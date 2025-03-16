import csv
from datetime import datetime
import os
from playwright.sync_api import sync_playwright
import time
import random

def ensure_screenshots_dir():
    """创建截图目录（如果不存在）"""
    screenshots_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)
    return screenshots_dir

def take_screenshot_with_highlight(page, element, filename):
    """为突出显示的元素拍摄截图"""
    # 用红色边框高亮元素
    page.evaluate("""(element) => {
        element.style.border = '3px solid red';
        element.style.backgroundColor = 'rgba(255, 0, 0, 0.2)';
    }""", element)
    
    # 拍摄截图
    screenshots_dir = ensure_screenshots_dir()
    filepath = os.path.join(screenshots_dir, filename)
    page.screenshot(path=filepath, full_page=True)
    
    # 移除高亮效果
    page.evaluate("""(element) => {
        element.style.border = '';
        element.style.backgroundColor = '';
    }""", element)
    
    return filepath

def fetch_github_trending(max_retries=3, timeout=60000):
    """
    使用Playwright获取并解析GitHub当日热门仓库。
    包含重试逻辑和超时设置。
    """
    trending_repos = []
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
    ]
    
    with sync_playwright() as p:
        browser_context_args = {
            "user_agent": random.choice(user_agents),
            "viewport": {"width": 1920, "height": 1080}
        }
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(**browser_context_args)
        page = context.new_page()
        
        retry_count = 0
        while retry_count < max_retries:
            try:
                # 设置较长的导航超时时间
                print(f"正在导航到GitHub热门页面（尝试 {retry_count + 1}/{max_retries}）...")
                page.goto("https://github.com/trending", timeout=timeout)
                
                print("等待仓库列表加载...")
                page.wait_for_selector("article.Box-row", timeout=timeout)
                
                # 在高亮前拍摄整页截图
                screenshots_dir = ensure_screenshots_dir()
                page.screenshot(path=os.path.join(screenshots_dir, "github_trending_full.png"), full_page=True)
                
                # 获取所有仓库文章
                repo_articles = page.query_selector_all("article.Box-row")
                print(f"页面上找到了 {len(repo_articles)} 个仓库。")
                
                for i, article in enumerate(repo_articles):
                    # 仓库名称和所有者
                    repo_name_element = article.query_selector("h2 a")
                    if repo_name_element:
                        full_name = repo_name_element.text_content().strip().replace("\n", "").replace(" ", "")
                        repo_href = repo_name_element.get_attribute("href")
                        repo_url = f"https://github.com{repo_href}"
                        
                        # 为突出显示的仓库名称拍摄截图
                        screenshot_path = take_screenshot_with_highlight(
                            page, 
                            repo_name_element, 
                            f"repo_{i+1}_{full_name.replace('/', '_')}.png"
                        )
                        print(f"已保存突出显示仓库的截图: {screenshot_path}")
                    else:
                        continue
                    
                    # 描述
                    description_element = article.query_selector("p")
                    description = description_element.text_content().strip() if description_element else "无描述"
                    
                    # 编程语言
                    language_element = article.query_selector("span[itemprop='programmingLanguage']")
                    language = language_element.text_content().strip() if language_element else "未知"
                    
                    # 星标和分支
                    stats = article.query_selector_all("a.Link--muted")
                    
                    stars = stats[0].text_content().strip() if len(stats) > 0 else "0"
                    forks = stats[1].text_content().strip() if len(stats) > 1 else "0"
                    
                    # 今日星标
                    today_stars_element = article.query_selector("span.d-inline-block.float-sm-right")
                    today_stars = today_stars_element.text_content().strip() if today_stars_element else "今日0颗星"
                    
                    trending_repos.append({
                        "repository": full_name,
                        "url": repo_url,
                        "description": description,
                        "language": language,
                        "stars": stars,
                        "forks": forks,
                        "stars_today": today_stars
                    })
                
                # 如果没有错误，我们就完成了
                break
                
            except Exception as e:
                retry_count += 1
                print(f"第{retry_count}次尝试出错: {e}")
                
                if retry_count < max_retries:
                    # 指数退避：每次重试等待更长时间
                    wait_time = 5 * (2 ** (retry_count - 1))
                    print(f"将在 {wait_time} 秒后重试...")
                    time.sleep(wait_time)
                else:
                    print(f"{max_retries}次尝试后失败。")
        
        browser.close()
    
    return trending_repos

def save_to_csv(repos, filename=None):
    """
    将仓库数据保存到CSV文件
    """
    if not filename:
        date_str = datetime.now().strftime("%Y%m%d")
        filename = f"github_trending_{date_str}.csv"
    
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ["repository", "url", "description", "language", "stars", "forks", "stars_today"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for repo in repos:
            writer.writerow(repo)
    
    return filepath

def main():
    print("使用Playwright获取GitHub热门仓库...")
    trending_repos = fetch_github_trending()
    
    if trending_repos:
        print(f"找到 {len(trending_repos)} 个热门仓库。")
        
        # 显示热门仓库
        for i, repo in enumerate(trending_repos, 1):
            print(f"\n{i}. {repo['repository']}")
            print(f"   URL: {repo['url']}")
            print(f"   描述: {repo['description']}")
            print(f"   语言: {repo['language']}")
            print(f"   星标: {repo['stars']} | 分支: {repo['forks']}")
            print(f"   {repo['stars_today']}")
        
        # 保存到CSV
        csv_path = save_to_csv(trending_repos)
        print(f"\n数据已保存至: {csv_path}")
    else:
        print("未找到热门仓库。")

if __name__ == "__main__":
    main()

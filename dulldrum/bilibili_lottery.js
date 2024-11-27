/**
 * 实现B站动态转发定时抽奖的小功能，增加下拉刷新功能
 * 作者: UP胖虎遛二狗 echonoshy@github.com
 * 使用方法: 
 * 1. 打开动态页面，在浏览器控制台粘贴本代码。
 * 2. 修改 `targetDate` 和 `drawCount` 配置参数，设置抽奖时间和抽奖人数。
 */

// ==================== 配置参数 ====================
const targetDate = new Date("2024-11-31T12:00:00"); // 设置抽奖时间
const drawCount = 3; // 设置抽奖人数
const scrollDelay = 500; // 下拉刷新的间隔时间（毫秒）
// =================================================

console.log("等待目标时间:", targetDate);

// 定时检查当前时间
const checkTimeInterval = setInterval(() => {
    const now = new Date();
    if (now >= targetDate) {
        clearInterval(checkTimeInterval); // 停止检查
        console.log("到达目标时间，开始抽奖操作！");

        // 执行抽奖逻辑
        startLottery();
    } else {
        console.log(`当前时间: ${now}，距离执行还有 ${(targetDate - now) / 1000} 秒`);
    }
}, 1000); // 每秒检查一次

// 全局变量，用于存储转发用户
let name_set = new Set(); 
let myScrollInterval; // 用于控制自动下拉刷新的循环

// 抽奖逻辑函数
function startLottery() {
    console.log("程序开始运行");

    // 自动点击“赞与转发”按钮
    const forwardTab = Array.from(document.querySelectorAll('.bili-tabs__nav__item')).find(el => 
        el.innerText.includes("赞与转发")
    );
    if (forwardTab) {
        forwardTab.click();
        console.log("点击了‘赞与转发’按钮，正在加载转发列表...");
    } else {
        console.error("未找到‘赞与转发’按钮，请检查页面是否正确！");
        return;
    }

    // 启动自动下拉刷新逻辑
    myScrollInterval = setInterval(scrollPage, scrollDelay);
}

// 自动下拉刷新
function scrollPage() {
    window.scrollBy(0, 1920); // 向下滚动一定距离

    const noMoreIndicator = document.querySelector(".reaction-list__nomore"); // 没有更多数据的指示器
    if (noMoreIndicator) {
        console.log("已到底部，停止下拉刷新");
        clearInterval(myScrollInterval); // 停止下拉刷新

        // 开始处理转发用户列表
        processForwardList();
    }
}

// 处理转发用户列表
function processForwardList() {
    console.log("开始处理转发用户列表...");

    const reactionItems = document.getElementsByClassName("reaction-item"); // 替换为实际转发用户列表选择器
    if (!reactionItems || reactionItems.length === 0) {
        console.error("未找到转发项，可能页面数据尚未加载或选择器错误！");
        return;
    }

    for (let i = 0; i < reactionItems.length; i++) {
        let reactionTextElement = reactionItems[i].getElementsByClassName("reaction-item__name")[0];
        if (reactionTextElement && reactionTextElement.innerText.includes("转发了")) {
            let name = reactionTextElement.innerText.replace("转发了", "").trim();
            name_set.add(name);
        }
    }

    console.log("抽奖数据加载完成，总共 " + name_set.size + " 名转发用户");
    console.log("用户列表：", Array.from(name_set));

    // 随机抽取幸运用户
    draw(drawCount); // 使用配置参数中的抽奖人数
}

// 抽取幸运用户
function draw(num) {
    // 将 name_set 转换为数组，以便操作
    const nameArray = Array.from(name_set);
    
    // 如果抽奖人数大于集合大小，直接限制抽奖人数
    if (num > nameArray.length) {
        console.log("抽奖人数大于用户数，自动调整为最大用户数！");
        num = nameArray.length;
    }

    // 用于存储已抽取的用户
    const winners = new Set();

    for (let i = 0; i < num; i++) {
        let luckyNum;

        // 直到抽到一个未抽过的用户
        do {
            luckyNum = Math.floor(Math.random() * nameArray.length); // 随机生成一个用户索引
        } while (winners.has(luckyNum)); // 如果用户已经被抽取，重新生成

        // 添加到已抽取用户集合
        winners.add(luckyNum);

        // 输出中奖者
        console.log(`🎉 中奖用户: ${nameArray[luckyNum]}`);
    }
}

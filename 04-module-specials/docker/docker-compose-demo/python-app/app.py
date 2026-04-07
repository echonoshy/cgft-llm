import time
import requests

while True:
    try:
        response = requests.get('http://nginx')
        print(f"Response from Nginx: {response.status_code}, Body: {response.text[:100]}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    
    time.sleep(3)  # 每隔3秒请求一次

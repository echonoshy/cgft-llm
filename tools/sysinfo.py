# 通过autodl提供api，监控服务器运行状态



import requests

token = "eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjM5NjU3MSwidXVpZCI6ImFlNmYwNGE5LTk0NTQtNGM3ZC04YjE3LTU1ZmRhOGM3ZTI1YSIsImlzX2FkbWluIjpmYWxzZSwiYmFja3N0YWdlX3JvbGUiOiIiLCJpc19zdXBlcl9hZG1pbiI6ZmFsc2UsInN1Yl9uYW1lIjoiIiwidGVuYW50IjoiYXV0b2RsIiwidXBrIjoiIn0.tv7JMMIg5nA-LhB7yYX9L8n9K6bYTwE-pplFsmMJHMQjEOGtww_Cqyd-BJpAJgIXyf8NopgGijLi2j5_uFcKBA"

headers = {"Authorization": token}
resp = requests.post("https://www.autodl.com/api/v1/wechat/message/send",
                     json={
                         "title": "autodl测试title",
                         "name": "autodl测试name",
                         "msg": "这是一段测试的代码",
                         "data": "这是一段测试的data"
                     }, headers = headers)
print(resp.content.decode())
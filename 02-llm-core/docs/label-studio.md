# AI 数据标注及label studio介绍


## 1. 数据标注

### 1.1 数据获取方式

- 公开数据集：hugging face, modelscope
- 外部采购
- 企业内打标 （数据安全与合规性要求）



### 1.2 训练数据标注流程

- 预处理
- 模型预打标 （可选）
- 标注数据质检
  - training set
  - test set



## 2. 本地化部署标注平台Label studio 

### 1. 安装

```bash
pip install label-studio 
```


### 2. 部署

> https://labelstud.io/guide/start
```
# 启动
nohup label-studio --data-dir ./data > nohup.out 2>&1 &

# 关闭
ps -ef | grep label-studio | grep -v grep | awk '{print $2}' | xargs kill -9
```

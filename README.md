# WaterSupplyMonitor
通知啥时停水。因为我们学校经常停水，导致大家十分烦恼：不知道啥时停水，不知道为啥停水，不知道啥时来水，所以做个通知服务。

### 数据来源
[武汉市水务集团有限公司－停水通知](http://www.whwater.com/gsfw/tstz/)

### 自用
- `pip install -r requirements.txt`
- `celery -A WaterSupplyMonitor worker -B -l info`

### 服务
- `pip install -r requirements.txt`
- `celery -A WaterSupplyMonitor worker -B -l info`
- `python AddInformURL.py`

### 关键词过滤

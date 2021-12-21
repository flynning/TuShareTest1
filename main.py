# 导入tushare
import tushare as ts
from matplotlib import pyplot as plt
import numpy as np

# 初始化pro接口
pro = ts.pro_api('a2dd50872bca0bcf417dc87193081aabb1645aadf7fc540e11d972c4')

# 拉取数据
df = pro.daily(**{
    "ts_code": "600021.SH",
    "trade_date": "",
    "start_date": "",
    "end_date": "",
    "offset": "",
    "limit": ""
}, fields=[
    "ts_code",
    "trade_date",
    "open",
    "high",
    "low",
    "close",
    "pre_close",
    "change",
    "pct_chg",
    "vol",
    "amount"
])
print(df)

plt.plot(df.change)
plt.plot(df.close)
plt.savefig("test.svg", format="svg")
plt.show()

rld = ts.get_realtime_quotes('600039')
rld=rld[['code', 'name', 'price', 'bid', 'ask', 'volume', 'amount', 'time']]
print(rld)

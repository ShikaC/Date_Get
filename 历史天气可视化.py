import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Pie,Bar,Timeline

df = pd.read_csv("台州2024天气.csv", encoding='utf-8')
# print(df["日期"])

df["日期"] = df["日期"].apply(lambda x: pd.to_datetime(x))
# print(df["日期"])

df["month"] = df["日期"].dt.month
# print(df["month"])

# 统计每个月中的各种天气出现的次数
df_agg = df.groupby(["month", "天气"]).size().reset_index()
# print(df_agg)

# 设置列名
df_agg.columns = ["month", "tianqi", "count"]
# print(df_agg)

# df_agg = df_agg[df_agg["month"]==1][["tianqi","count"]]
# df_agg = df_agg.sort_values(by="count",ascending=False).values.tolist()
# print(df_agg)


# 画图
timeline = Timeline()
timeline.add_schema(play_interval=1000)# 单位毫秒

for month in df_agg["month"].unique():
    data = (
        df_agg[df_agg["month"]==month][["tianqi","count"]]
        .sort_values(by="count",ascending=True)
        .values.tolist()
    )

    bar = Bar() #柱状图
    # x:天气名称
    bar.add_xaxis([x[0] for x in data])
    # y:出现次数
    bar.add_yaxis("",[x[1] for x in data])

    bar.reversal_axis()#横着

    #计数标签放在图形右边
    bar.set_series_opts(label_opts=opts.LabelOpts(position="right"))

    # 设置图表名称
    bar.set_global_opts(title_opts=opts.TitleOpts(title="台州2024每月天气变化"))

    timeline.add(bar,f"{month}月")
    # 保存图表
    timeline.render("weather.html")

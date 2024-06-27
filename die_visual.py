from die import Die
import plotly.express as px

# 创建两个DF
die_1 = Die()
die_2 = Die()


results = []
# 把每次掷骰子的结果加入数组中
for roll_num in range(100):
    result = die_1.roll()+die_2.roll()
    results.append(result)

print(results)

'''统计每个点数出现的次数'''
frequences = []
max_result = die_1.num_sides + die_2.num_sides
poss_result = range(2, max_result+1)
for value in poss_result:
    frequences.append(results.count(value))

print(frequences)

# 画出条形图
# 定制坐标轴title等
title = "Results of Rolling Two D6 Dices 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_result, y=frequences, title=title, labels=labels)
# 让条形图刻度间距为1
fig.update_layout(xaxis_dtick=1)
fig.show()





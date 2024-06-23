from die import Die
import plotly.express as px

die = Die()

results = []
# 把每次掷骰子的结果加入数组中
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)

'''统计每个点数出现的次数'''
frequences = []
poss_result = range(1, die.num_sides+1)
for value in poss_result:
    frequences.append(results.count(value))

print(frequences)

# 画出条形图
# 定制坐标轴title等
title = "Results of Rolling One D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_result, y=frequences, title=title, labels=labels)
fig.show()





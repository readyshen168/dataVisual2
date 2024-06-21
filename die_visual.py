from die import Die

die = Die()

results = []
# 把每次掷骰子的结果加入数组中
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)
import datetime

print(" ")
year = int(input("Enter the year you want to calculate from: "))
month = int(input("Enter the month you want to calculate from: "))
day = int(input("Enter the day you want to calculate from: "))
print(" ")

date1 = datetime.datetime(year, month, day)
date2 = datetime.datetime.now()
delta = date2 - date1

power_cost = 80.23
power_usage = int(input("Enter how much you use each day (Kwh): "))
print(" ")

cost_per_hour = power_cost * (power_usage / 24)
cost_per_day = cost_per_hour * 24

while True:
    cost_split = str(cost_per_day / 100).split(".")
    cost_split_0 = str(cost_split[0])
    pre_cost_split_1 = []

    for num in (cost_split[1]):
        pre_cost_split_1.append(num)

    final_cs_1 = pre_cost_split_1 [:2]
    final_cs_1.append(".")

    last_cs_1 = []
    last_cs_1 = pre_cost_split_1 [2:]

    for e in last_cs_1:
        final_cs_1.append(e)
    
    cost_split_1 = str(final_cs_1[0] + final_cs_1[1] + final_cs_1[2] + final_cs_1[3])

    print("cost per day: ", str(cost_split_0), "kr", str(cost_split_1), "öre")
    break

while True:
    
    total_cost = cost_per_day * (delta.days)

    cost_split = str(total_cost / 100).split(".")
    cost_split_0 = str(cost_split[0])
    pre_cost_split_1 = []

    for num in (cost_split[1]):
        pre_cost_split_1.append(num)

    final_cs_1 = pre_cost_split_1 [:2]
    final_cs_1.append(".")

    last_cs_1 = []
    last_cs_1 = pre_cost_split_1 [2:]

    for e in last_cs_1:
        final_cs_1.append(e)

    print("Total cost: ", str(cost_split_0), "kr", str(cost_split_1), "öre")
    print(" ")
    break
    
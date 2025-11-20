marks={
    "101":[20,30,40],
    "102":[24,10,20],
    "103":[17,20,20],
}
# get the average and sum of marks in two different dicts
total={}
avg={}
for i in marks.keys():
    total[i]=sum(marks[i])
    avg[i]=sum(marks[i])/len(marks[i])

print(total)
print(avg)
# print(sum(marks['101']))
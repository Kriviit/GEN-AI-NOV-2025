#loops DRY -> DONT repeat yourself
#  Hard coded

# while
# for
# 1 2 3 4 5 6 7 8 9 10
start=1
stop=10
jump=10
print("start loop")
while(start<=stop):#condition t t ... False
    print(start)# 1 2 3 4....10
    start+=1# updation 2 3 .....11
print("loop ended")



# for -> provide me a collection(list,tuple,range) i will run n(no of elements in collection) times each time i itrate 
# i will take that nth value in varable
# for var in collection
arr=[12,22,33,44,True,False]

for i in arr:
    print(i)
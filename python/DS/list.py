# # a=[1,2,3]
# # b=[3,4,5]
# # print(a+b)
# # print(a*3)
# # print(a[2])
# # print(a[-1])

# arr=[10,20,30,40,50,60,70,80,90,100]
# print(max(arr))
# print(min(arr))
# print(sum(arr))
# print(len(arr)) #no of elements in that collection
# # sub_list=arr[::2]#step=1 START=0 # [10,30,50,70,90]#CREATED
# # print(sub_list)

# print(dir([]))
# # print(dir([123]))


#any method if it is modifing the existing obj -> None
#any method if it is doest modifing the existing obj -> somthing

# arr1=[1,2,3,4]#list
# arr1.append(20)
# print(arr1)#[1,2,3,4,20]
# result=arr1.clear()#None
# print(result)
# print(arr1)

# a=[1,2,3,4]
# b=a##same object
# a.append(20)
# print(b)

# ar=[1,12,13,22,13]
# b=ar.copy()#new list with similar data as object
# c=ar[:]#opertors->new list
# ar.append(20)
# print(b)
# print(ar)

# arr=[1,2,1,2,1,22,2,3,1,2,3,1,2,32,2,1]
# count_of_3=arr.count(2)
# print(count_of_3)


arr1=[1,2,3,4]
arr2=[12,22,33,44]
# # arr1.append(arr2)
# arr1.extend(arr2)
# print(arr1.index(33))
# arr2.remove(33)# based on value
# print(arr2)
# print(arr2.pop(0))
arr2.reverse()
print(arr2)
arr2.sort(reverse=True)
print(arr2)
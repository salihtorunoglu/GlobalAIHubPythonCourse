myList=[1,3,5,7]
myList1=[2,4,6,8]
myList.extend(myList1) #First I extended myList with myList1
print(myList)
multiplied_list = [element * 2 for element in myList] #Then I multiplied the extended list with two
print(multiplied_list)
for i in multiplied_list:
    print(i,"=",type(i))   #At last I printed the type of the list element

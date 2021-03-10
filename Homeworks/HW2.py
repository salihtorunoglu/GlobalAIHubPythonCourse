MyList1 = [1,3,5,7]
MyList2 = [2,4,6,8]
MyList1.extend(MyList2) #I extended MyLis1 with MyList2
print(MyList1) #I printed the extended list
Multiplied_List=[element*2 for element in MyList1] #I mutiplied every variable in extended list with two
print(Multiplied_List)
for i in Multiplied_List: #I used a loop to print the data type of the all values in Multiplied_List
    print(i,"=",type(i))

myList=['A','B','C']

print('The list is : ',myList)
print('The length of list is : ',len(myList))

print('Now we will split this array, the items of this array is - ')
for item in myList:
    print(item)

#strIndex=input('Tell me what item do you want, please input an index from 1 to '+str(len(myList))+' : ')
strIndex='0'
index=0
try:
    index=int(strIndex)
        
    if index<1 and index>len(myList):
        print('index invalid')
    else:
        print('The item you selected is: ',myList[index-1])

except TypeError:
    print('Fail to convert the type')
except:
    print('Fail to get the index you input')

myList[0]='AA'
print(myList)

#update value start from index:1 to 3 (not include), totally 2 items
myList[1:3]=['BB','CC']
print(myList)

#If you insert more items than you replace, the new items will be inserted where you specified
myList[1:2]=['BBB','DDD']
print(myList)

#If you insert less items than you replace, 
# the new items will be inserted where you specified, and the remaining items will move accordingly
myList[1:3]=['BBBB']
print(myList)

#insert item in specified index
myList.insert(3,'DDD')
print(myList)

myList.append('EEE')
print(myList)

myList.append('DDD')
print(myList)

myList.remove('EEE')
print(myList)

#Remove the first occurance of match word
myList.remove('DDD')
print(myList)

myList.append('DDD')
myList.pop(3)
print(myList)

myCopyList=myList.copy()
print(myCopyList)
myCopyList.clear()
print(myCopyList)

myCopyList=myList.copy()
print(myCopyList)
del myCopyList
#print(myCopyList)

myList=[1,10,5,6,8,3,2]
myList.sort()
print(myList)

myList.sort(reverse=True)
print(myList)

list1=['a','b','c']
list2=[1,2,3]
list3=list1+list2
print(list3)

list1.extend(list2)
print(list1)
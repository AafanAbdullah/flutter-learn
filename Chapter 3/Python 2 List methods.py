#Add one element at the end
list =[ 5,6,3]
print(list.append(4))
print(list)


#Sort in ascending order
list = [7,6,2,4,1]
print(list.sort())
print(list)

#Sort in descending order
list = [8,7,3,1,2,5]
print(list.sort(reverse=True))
print(list)

#Reverse list
list = ['a','b','c','d','e','f']
list.reverse()
print(list)

#insert element at index
list = [3,2,1]
list.insert(1,5)
print(list)

#remove first occurance of the element
list = [2,1,3,1]
list.remove(1)
print(list)

#removes element in index
list = [2,1,3,1]
list.pop(2)
print(list)
lst=['apple','guava','papaya','grape','banana']
print("Length of the list:",len(lst))
print("First element:",lst[0])
print("Last element:",lst[-1])

lst.append('mango')
print("Appended list:",lst)
lst.remove('banana')
print("Removed list:",lst)
lst.sort()
print("Sorted list:",lst)
lst.pop(2)
print("Popped list:",lst)
lst.reverse()
print("Reversed list:",lst)
print("Multiplication of list:",lst*2)

lst=lst[:-2]
print("Sliced list:",lst)

lst.clear()   
print("Updated list:",lst)


my_dict={}
my_dict={1:'apple',2:'guava'}

my_dict={'name':'Jack',1:[1,2,3,4]}
my_dict={'name':'John','age':26}

print(my_dict['name'])
print(my_dict['age'])

my_dict['age']=27
print(my_dict)
my_dict['address']='Downtown'
print(my_dict)


my_dict.pop('age')
print(my_dict)

print("Address:",my_dict.get("address"))

my_dict.clear()
print(my_dict)


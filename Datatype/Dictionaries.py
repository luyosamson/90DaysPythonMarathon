#It is a collection of values,items or objects of different types stored in 
#key vale pairs enclosed in curly  braces and each key is  separated from its
# value by a colon

#Characteristics
        #Are ordered in python 3.7
        #Can store various types of elements
        #Elements cannot be accessed by index
        #Are mutable-Can change or remove item after dict have been created
        #Does not allow duplications
lang={1:'Java',2:'JavaScript',3:'Python', 4:'Ruby',5:'Scala',6:'C++',7:'Nodejs'}

print(lang)

print(lang[4])
print(lang.get(3))
print(lang.pop(5))
print(lang)
print(len(lang))
print(sorted(lang))

print(lang.values())
lang.update({5:'Pascal'})
print(lang)
lang.popitem()
print(lang)

for a,b in lang.items():
    print(a,b)

lang2=lang.copy()
print(lang2)
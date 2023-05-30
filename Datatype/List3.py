furniture='Desk','Table','Chair','Shelf'
price=[1000,600,900,1200]
name=['Samson','Omondi','Luyo','Kevin']

for item,owner,cost in zip(furniture,name,price):
    print(f'The {item},belongs to {owner} is costing ${cost}')

print(furniture)

a,b='samson','jacky'
a,b=b,a
print(b)

furniture.index('Chair')
furniture=['table','chair','shelf','drawer','rack']
l=len(furniture)
print(l)
furniture[2]='desk'
print(furniture)
numbers=['1','2','4','6','8']

myList=numbers+furniture
print(myList)

for index,item in enumerate(myList):
    print(f"Index :{index}-item:{item}")
    
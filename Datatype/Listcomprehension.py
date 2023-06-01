name=['Samson','Luyo','Omondi','Mary','Victor','Samwel','Samo']
marks=[23,5,78,90,32]
# new_name=[]
# for n in name:
#     new_name.append(n)
#     print(n)

# new_name=[]
# for n in name:
#     if n.startswith('S'):  
#         new_name.append(n)
# print(n)


new_marks=[num*2 if num %2 == 0 else num for num in marks]
print(new_marks)

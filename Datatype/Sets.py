#Items are not in a particular orders
#No duplicate items are allowed
#Items must be imuutable objects


#Set remove duplicate items,so cat will only appear onces

animals={'Dog','Elephant','Tiger','Pig','Cat','Zebra','Cat'}
print(animals)

plants={'Rose','Palm','Fig'}

# Adding a list in a set

animals.update(plants,{'Luyo'})

print(animals)

#remove Items from the set
#both discard and remove are used to remove items from a set
#remove through an error when the item is not in the set,while discard returns null
#Clear remove everything from the set at once

animals.discard('Luyo')
print(animals)

#Using union

leo=animals | plants
print(leo)

#Intersection
#We can use intersection method or &(ampasand)
flowers={'Rose','Hibiscus','Bouganvillea','Lilly'}
insects = {'Bee', 'ButterFly', 'tsetse fly', 'Hibiscus'}

life=flowers.intersection(insects)
print(life)

life2=flowers & insects
print(life2)
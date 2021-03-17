thisset  = {"apple", "banana", "cherry"}
print(type(thisset))

for x in thisset:            #Loop through the set, and print the values:
  print(x)

  print("banana" in thisset)         #Check if "banana" is present in the set:
                                     #Once a set is created, you cannot change its items, but you can add new items.

thisset.add("orange")
print(thisset)                           #Add an item to a set, using the add() method:


tropical = {"pineapple", "mango", "papaya"}        #Add elements from tropical and thisset into newset:
thisset.update(tropical)
print(thisset)


thisset.remove("banana")               #Remove "banana" by using the remove() method:
print(thisset)

""" thisset.clear()

print(thisset)                        #The clear() method empties the set:



del thisset

print(thisset)




The union() method returns a new set with all items from both sets:

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)



The update() method inserts the items in set2 into set1:
set1.update(set2)
print(set1)


Keep the items that exist in both set x, and set y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)"""



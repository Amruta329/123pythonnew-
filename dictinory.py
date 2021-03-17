thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])


#Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020                      #this will update the value
}
print(thisdict)


#Print the number of items in the dictionary:

print(len(thisdict))


#The values in dictionary items can be of any data type:
#String, int, boolean, and list data types:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]

}
print(type(thisdict))


x = thisdict["year"] 
print(x)         #this will print the value of model key
x = thisdict.get("year")      #this will print the value of model key same output
print(x)


#Get a list of the keys:

x = thisdict.keys()
print(x)

#Get a list of the values:

x = thisdict.values()
print(x)

#add new item in dictionory
thisdict["color"] = "red"
print(thisdict)


#Check if "model" is present in the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

  thisdict["color"] = "red"              #add the items
print(thisdict)


"""thisdict.pop("model")             #The pop() method removes the item with the specified key name:

thisdict.popitem()
print(thisdict)                      #he popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

del thisdict["model"]
print(thisdict)                      #The del keyword removes the item with the specified key name:


del thisdict
print(thisdict)                        #this will cause an error because "thisdict" no longer exists.


thisdict.clear()
print(thisdict)                                       #The clear() method empties the dictionary:"""




thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)                    #Loop through both keys and values, by using the items() method:

mydict = thisdict.copy()            #copy the elements 
print(mydict)


mydict = dict(thisdict)             #copy using dict function
print(mydict)






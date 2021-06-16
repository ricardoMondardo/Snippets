dicOne = {
    "1": "ccc",
    "2": "abc"
}

print("\nObj:")
print(dicOne)
print("\n")

print("Print all values in the dictionary, one by one:\n")
for x in dicOne:
    print(dicOne[x])
print("\n")    

print("You can also use the values() function to return values of a dictionary:\n")
for x, y in dicOne.items():
  print(x, y)    
print("\n")  

print("Loop through both keys and values, by using the items() function:\n")
for x in dicOne.values():
  print(x) 
print("\n")   



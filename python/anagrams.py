arr = ["Code","test","try","Coed","Time","Item"]
result = {}

for i in arr:
    sorted_characters = sorted(i.lower())
    str_sorted = ''.join(sorted_characters)
    if (result.get(str_sorted) == None):
        result[str_sorted] = 1
    else:
        result[str_sorted] = result[str_sorted] + 1

print(result)
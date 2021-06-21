# Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false.
# For example: if strArr contains ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"] the output should return "1,4,13" because those numbers appear in both strings. The array given will not be empty, and each string inside the array will be of numbers sorted in ascending order and may contain negative numbers.

def getInterArr(arrBigger, arrCheck):
  result = []
  
  for v in arrBigger:
    for y in arrCheck:
      if v == y:
        result.append(int(v))

  return sorted(result)

def FindIntersection(strArr):

  # code goes here

  arrOne = strArr[0].replace(' ', '').split(',')
  arrTwo = strArr[1].replace(' ', '').split(',')

  if (len(arrOne) > len(arrTwo)):
    result = getInterArr(arrOne,arrTwo) 
  else:
    result = getInterArr(arrTwo,arrOne) 

  return ','.join(map(str, result)) if len(result) > 0 else False

# keep this function call here 
print(FindIntersection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]))
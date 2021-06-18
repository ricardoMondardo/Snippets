def BracketMatcher(strParam):

  
  CleanArr = list(filter(lambda x : x == '(' or x == ')' , list(strParam)))
  count = 0

  if len(CleanArr) == 0: 
    return 1

  for i in CleanArr:
    if i == '(':
      count += 1
    else:
      count -= 1
    if count < 0: 
      return 0

  return 1 if count == 0 else 0

# keep this function call here 
print(BracketMatcher("hello()"))
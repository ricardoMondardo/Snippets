# Have the function BracketCombinations(num) read num which will be an integer greater than or equal to zero, and return the number of valid combinations that can be formed with num pairs of parentheses. For example, if the input is 3, then the possible combinations of 3 pairs of parenthesis, namely: ()()(), are ()()(), ()(()), (())(), ((())), and (()()). There are 5 total combinations when the input is 3, so your program should return 5.

def Fact(n):
   
  if (n == 1):
    return 1
  else:
    return n * Fact(n-1)  

def BracketCombinations(num):

    num  = Fact(num)

    return num

print(BracketCombinations(3))
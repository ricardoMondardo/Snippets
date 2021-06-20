import re

def LongestWord(sen):
  
  longestWord = ""

  for word in sen.split(' '):    
    
    wordArr = []    
    for l in word:
      if l.isalpha() or l.isnumeric():
        wordArr.append(l)

    if len(wordArr) > len(longestWord):
      longestWord = ''.join(wordArr)
   
  return longestWord

# keep this function call here 
print(LongestWord("aa fun&!! time1 aaa kk sssssss kkjs"))
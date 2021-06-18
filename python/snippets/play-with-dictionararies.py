text = "code test try code time item and for banana fade brand i face new all she here car"
arrWord = text.split(" ")

rDic = {}

for word in arrWord:
  lenWord = len(word)

  if lenWord in rDic:
    rDic[lenWord].append(word)
    rDic[lenWord] = sorted(rDic[lenWord])
  else: 
    rDic[lenWord] = [word]

rDic = sorted(rDic.items(),reverse=True)    

for k, v in rDic:
  print(k,v)



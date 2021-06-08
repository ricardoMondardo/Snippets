text = "9 \ncode test try code time item and for banana fade brand i face new all she here car"

cleanText = text[text.find('\n')+1:]
arrText = cleanText.split(' ')

maxCountLine = int(text[0:text.find('\n')])

currentLineCount = 0
result = ""

for word in arrText:

    lenWord = len(word)
    currentLineCount = currentLineCount + lenWord    
    firstWordLine = (currentLineCount == lenWord)
    
    if (currentLineCount < maxCountLine):
        if (firstWordLine):
            result += word
        else:
            result += ' ' + word
            # count space as char
            currentLineCount = currentLineCount + 1
    else:     
        result += '\n' + word
        currentLineCount = len(word)

    # print(currentLineCount, maxCountLine)        
    # print(result)

print(result)


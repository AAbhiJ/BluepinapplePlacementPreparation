# Convert Number to Words

def convertToWord(number):
    if(int(number)==0):
        return "Zero"
    WordString = ""
    numberStrings = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen"
    ,"Nineteen"]
    tensString = ["","","Twenty","Thirty","Fourty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    tenMultipleString = ["","","Hundred ","Thousand ","Thousand"]
    tensMultipleCount = 0

    if(int(number)<=19):
        return (numberStrings[int(number)])
    else:
        LastTwoDigits = int(number[-2:])
        startingDigit = 0
        if(LastTwoDigits<=19):
            startingDigit=2
            WordString = numberStrings[LastTwoDigits]
            tensMultipleCount+=2
        number = number[::-1]
        for i in range(startingDigit,len(number)):
            digit = int(number[i])
            if(i>=2):
                if(digit!=0):
                    WordString = tenMultipleString[tensMultipleCount] + WordString
            if(i%2!=0 and tensMultipleCount==1):
                WordString = tensString[digit]+WordString
            else:
                WordString = numberStrings[digit] +  WordString
            tensMultipleCount+=1
    return WordString


if __name__ == '__main__':
    number = input("Enter a amount : ")
    if(number.isnumeric()):
        if(len(number)<1):
            print("Wrong number Entered!")
        else:
            word = convertToWord(number)
        print(word)
    else:
        print("Not a number")


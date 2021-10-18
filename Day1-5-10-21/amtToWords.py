# Convert Number to Words
import math
def toHundreds(number):
    # print(number)
    numberStrings = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen"
    ,"Nineteen"]
    tensString = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
    word = ""
    length = len(number)
    twoDigits = int(number[-2::])
    if(len(number)==3):
        word = word + numberStrings[int(number[length-3])]
        if(int(number[length-3])!=0):
            word += "Hundred "
    if(twoDigits <= 19):
        word += numberStrings[twoDigits]
    else:
        word = word + tensString[int(number[length-2])] + numberStrings[int(number[length-1])]
    return word


def convertToWord(number):
    n = len(number)
    if(int(number)==0):
        return "Zero"
    WordString = ""
    tenMultipleString = ["","Thousand ","Million ","Billion ","Trillion ","Quadrillion ","Quintillion ","Sextillion ","Septillion ","Octillion ","Nonillion ","Decillion ","Undecillion ","Duodecillion ","Tredecillion ","Quattuordecillion "]
    for i in range(math.ceil(len(number)/3)):
        returnedWord = toHundreds(number[-3*(1+i):n-(3*i):]) 
        if(returnedWord!=""):
            WordString = tenMultipleString[i] + WordString 
        WordString = returnedWord + WordString
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


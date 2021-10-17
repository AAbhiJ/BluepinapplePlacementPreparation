# Write a program to print all perfect numbers between 1 to n

def generateMatrix(n):
    divisorMatrix = [[] for i in range(n+1)]
    for i in range(1,(n+2)//2):
        for j in range(i,n+1,i):
            if(i!=j):
                divisorMatrix[j].append(i)
    return divisorMatrix

def getPerfectNumbers(n):
    divisorMatrix = generateMatrix(n)
    perfectNumbers = []
    for i in range(len(divisorMatrix)):
        if(i==28):
            print(divisorMatrix[i],i)
        if(sum(divisorMatrix[i])==i):
            perfectNumbers.append(i)
    # print(divisorMatrix)
    # for i in divisorMatrix:print(i,end=" ")
    return perfectNumbers[1:]

if __name__ == '__main__':
    n = int(input())

    perfectNumbers = getPerfectNumbers(n)
    for i in perfectNumbers:print(i,end=" ")

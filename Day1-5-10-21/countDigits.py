# Find total occurrences of each digits (0-9) using function.

def countDigits(number):
    counts = [0]*10
    print(f"cnt 1 {counts[0]}")
    for i in number:
        counts[int(i)]+=1
    return counts


if __name__ == '__main__':
    number = input()
    digitCounts = countDigits(number)
    print("Digits and there count : \n\tDigit\tCount")
    for digit in range(len(digitCounts)):
        print(f"\t{digit}\t{digitCounts[digit]}")

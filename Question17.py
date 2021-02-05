myDict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
          11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
          10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred", 1000: "thousand"}

for i in range(1, 1001):
    if i <= 100:
        if i not in myDict:
            newNum = i // 10 * 10
            myDict[i] = myDict[newNum] + myDict[i % 10]
    elif i < 1000:
        newNum = i // 100
        newNum1 = (newNum * 100) // newNum
        if i % 100 != 0:
            myDict[i] = myDict[newNum] + myDict[newNum1] + "And" + myDict[i % 100]
        else:
            myDict[i] = myDict[newNum] + "And" + myDict[newNum1]

count = 0
for i in myDict.values():
    count += len(i)
print(count)

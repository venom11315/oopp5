#loop bicycle numbers into numlist to save the numbers available for users to pick
#file
import random
class rem:
    def remove(self):
        storage = open('storage.txt', 'r')
        lines = [line.split(",") for line in storage]
        numList2 = []
        for num in lines:
            lastsec = int(num[2])
            numList2.append(lastsec)
        numList = []
        for x in range(1,701):
            numList.append(x)
        for i in numList2:
            for j in numList:
                if j == i:
                    numList.remove(j)
        rand = random.choice(numList)
        return rand

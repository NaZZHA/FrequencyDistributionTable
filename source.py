import math, os
from texttable import Texttable

title = "Frequency Distribution Table"
author = "W. Santos"
version = 1.0

print("Title: " + title)
print("Author: " + author)
print("Version: {0}".format(version) + "\n")

size = int(input("Size:>> "))
data = list()
clear = lambda: os.system('cls')

#sample data from pg 59
#tempData = [105, 94, 95, 85, 103, 94, 100, 99, 86, 85, 96, 86, 107, 107, 115, 105, 86, 96, 115, 107,
#            87, 95, 85, 95, 120, 105, 106, 117, 96, 99, 115, 85, 86, 89, 117, 116]

for i in range(size):
    data.append(int(input('add: ')))

highestData = max(data)
lowestData = min(data)
rangeVal = highestData - lowestData
n = int(1 + (3.3 * math.log10(len(data))))
intervalSize = int(rangeVal / n)
maxSize = len(data)
lowerLimit = lowestData

intervals=[] #intervals !IN STRING!
cb=[]        #Class Border
lo=[]        #Lower limits of intervals
hi=[]        #Upper limits of intervals
freq=[]      #Frequency
gcf=[]       #<CF
lcf=[]       #>CF
cm=[]        #Class Mark
relf=[]      #Relative Frequency

for i in range(n):
    freq.append(0)
    cm.append(0)
    relf.append(0)

for i in range(n):
    lo.append(lowerLimit)
    hi.append(lowerLimit + intervalSize)
    intervals.append('{0} - {1}'.format(lowerLimit, lowerLimit + intervalSize))
    cb.append('{0} - {1}'.format(lowerLimit - 0.5, lowerLimit + intervalSize + 0.5))
    lowerLimit = lowerLimit + intervalSize + 1

for i in data:
    for val in range(len(hi)):
        if(i <= hi[val] and i >= lo[val]):
            freq[val] += 1

for i in range(n):
    relf[i] = ( round((freq[i] / len(data)) * 100 , 1))

first = True
lastv = None
cont = 0
for i in freq:
    if(first):
        gcf.append(i)
        first = False
    else:
        gcf.append(i + lastv)

    lastv = gcf[cont]
    cont += 1

first = True
lastv = 0
cont = 0

for i in range(n):
    if(first):
        lcf.append(maxSize)
        first = False
    else:
        lcf.append(abs(lastv - freq[cont]))
    lastv=lcf[i]

for i in range(n):
    cm[i] = (round( (hi[i] + lo[i]) / 2, 1))

#print everything
table = Texttable()
values = Texttable()

table.add_row(["intervals", "Frequency", "Rel. Frequency", "Class Mark", "Class Border", "<CF"])

values.add_row(["Range", "Number of Intervals", "Class Size"])
values.add_row([rangeVal, n, intervalSize])

for i in range(n):
    table.add_row([intervals[i], freq[i], relf[i], cm[i], cb[i], gcf[i]])

clear()
print(values.draw())
print("")
print(table.draw())
input()

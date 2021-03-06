import math, os
from texttable import Texttable
from sys import platform

title = "Frequency Distribution Table"
author = "W. Santos"
version = '1.3'

debug = False
defaultSort = 'HighestToLowest'
sort = defaultSort

print("Title: " + title)
print("Author: " + author)
print("Version: {0}".format(version) + "\n")

if debug == True:
    print('\nPROGRAM RUNNING IN DEBUG MODE')
    print('USING DEFAULT DATA VALUES')
    input()
data = []
size = 0

if debug == True:
    data = [105, 94, 95, 85, 103, 94, 100, 99, 86, 85, 96, 86, 107, 107, 115, 105, 86, 96, 115, 107,
            87, 95, 85, 95, 120, 105, 106, 117, 96, 99, 115, 85, 86, 89, 117, 116]
else:
    size = int(input("Size:>> "))
    for i in range(size):
        data.append(int(input('add: ')))

if debug == False:
    sortIn = input('\nHow would you like your table to be sorted \n Type HighestToLowest or LowestToHighest \n\n:')
    if sortIn == 'HighestToLowest':
        sort = defaultSort
    elif sortIn == 'LowestToHighest':
        sort = 'LowestToHighest'

clearWindows = lambda: os.system('cls')
clearLinux = lambda: os.system('clear')

highestData = max(data)
lowestData = min(data)
rangeVal = highestData - lowestData
n = int(1 + (3.3 * math.log10(len(data))))
intervalSize = int(rangeVal / n)
maxSize = len(data)
lowerLimit = lowestData

intervals=[]    #intervals !IN STRING!
cb=[]           #Class Border
lo=[]           #Lower limits of intervals
hi=[]           #Upper limits of intervals
freq=[]         #Frequency
gcf=[]          #<CF
lcf=[]          #>CF
cm=[]           #Class Mark
relf=[]         #Relative Frequency

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
lastv = maxSize
cont = 0

for i in range(n):
    if first:
        lcf.append(lastv)
        first = False

    elif i >= 1:
        if i == n:
            lcf.append(lastv - freq[i])
        else:
            lcf.append(lastv - freq[i-1])

        lastv = lcf[i]
    cont += 1

for i in range(n):
    cm[i] = (round( (hi[i] + lo[i]) / 2, 1))

#print everything

if debug == False and sort == 'HighestToLowest':
    intervals.reverse()
    lo.reverse()
    hi.reverse()
    freq.reverse()
    gcf.reverse()
    lcf.reverse()
    cm.reverse()
    relf.reverse()
    cb.reverse()

table = Texttable()
values = Texttable()
dataOutput = Texttable()

table.header(["intervals", "Frequency", "Rel. Frequency", "Class Mark", "Class Boundary", "<CF", ">CF"])
table.set_chars(['=', ' ', ' ', '='])

table.set_header_align(["c","c","c","c","c","c","c"])
table.set_cols_valign(["c","c","c","c","c","c","c"])

values.add_rows([["Range", rangeVal],
                ["No. of Intevals", n],
                ["Class Size", intervalSize]], header=False)

values.set_cols_align(["c","c"])
values.set_chars(["="," ","="," "])

for i in range(n):
    table.add_row([intervals[i], freq[i], relf[i], cm[i], cb[i], gcf[i], lcf[i]])

if platform == "linux" or platform == "linux2":
    clearLinux()
else:
    clearWindows()


print(data)
print("")
print(values.draw())
print("")
print(table.draw())
input()

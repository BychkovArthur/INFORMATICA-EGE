string = open('24 (3).txt').readline()
for i in '0123456789':
    string = string.replace(i, ' ')
string = string.split()
mxCnt = 0
dayNum = 0
currDay = 0
for sub in string:
    currDay += 1
    if sub.count('BOBR') > mxCnt:
        mxCnt = sub.count('BOBR')
        dayNum = currDay
print(dayNum)
        

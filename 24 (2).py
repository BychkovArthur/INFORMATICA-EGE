string = open('24 (2).txt').readline()
mx = 0
for start in range(7, 15):
    count = 0
    for i in range(start, len(string), 8):
        if string[i-7:i+1] in ['FLASHEGE', 'EGEFLASH']:
            count += 1
            mx = max(mx, count)
        else:
            count = 0
print(mx)

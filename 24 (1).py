string = open('24 (1).txt')
addresses = set()
for sub in string:
    sub1 = sub.strip().split('.')
    if sub1[0] == '192' and sub1[2][:2] == '15':
        addresses |= {sub.strip()}
print(len(addresses))
    

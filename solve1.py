f = open('task1.txt')

ans = 0

for s in f: #1
    slist = [int(x) for x in s.split()]#2 

    kr7 = 0
    
    for i in range(len(slist)):#3
        if abs(slist[i]) %7 == 0:#4
            kr7 += 1#5

    slist.sort()#6
    
    if (  slist[2] > (slist[0] + slist[1])  ):#7
        if kr7 >= 2:#8
            ans += 1

print(ans)
        
    
    

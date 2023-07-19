f = open('task2.txt')

ans = 0

for s in f: #1
    str_num = s.split()#2
    slist = [int(x) for x in str_num]#3
    
    n3 = 0
    n2 = 0
    positive_sum = 0
    
    for i in range(len(slist)):#4
        if (abs(slist[i]) >= 100 and abs(slist[i]) <= 999) :#5
            n3 += 1
        if (abs(slist[i]) >= 10 and abs(slist[i]) <= 99):#6
            n2 += 1
        
        if slist[i] > 0:#7
            positive_sum += slist[i]

    if ( positive_sum >= 10 and positive_sum <= 99) and positive_sum%2 != 0:#8
        if ( n3 >= 1 and n2 >= 1 ):#9
            ans += 1#10

print(ans)
        

f = open('task3.txt')
ans = 0
str_i = 0

for s in f:#1
    str_i += 1
    
    s_num = s.split()#2
    slist = [int(x) for x in s_num]#3

    n2 = []
    n0 = []

    for i in range(len(slist)):#4
        
        if slist.count(slist[i]) == 2:#5
            n2.append(slist[i])     
        if slist.count(slist[i]) == 1:#6    
            n0.append(slist[i])
    
    if len(n2) == 4 and len(n0) == 4:#7
        chet = set(n2)#8
        chet = list(chet)
        
        if chet[0]%2 == chet[1]%2 :#9  
            sr = sum(n2)//len(n2) #10
         
            if sr%2 != str_i%2:#11
                ans += 1
print(ans)

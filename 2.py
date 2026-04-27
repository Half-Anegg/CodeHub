for i in range(2):
    n=int(input())
    pack=[]
    check=[]
    flag=[]
    m=0
    for j in range(n):
        pack.append(list(map(int,input().split(','))))
        if pack[j][0]>m or pack[j][1]>m:
            m=max(pack[j][0],pack[j][1])
    for j in range(m):
        check.append([0,0,0])
        flag.append(0)
    for j in range(n):
        check[pack[j][0]-1]=[pack[j][0]-1,pack[j][1]-1]
    circle=False
    for j in range(n):
        s=0
        finding=True
        while finding:
            if flag[check[s][1]]!=1:
                flag[check[s][1]]=1
            else:
                print("false")
                circle=True
                break
            if(check[check[s][1]][1]!=0):
                s=check[check[s][1]][1]
            else:
                for k in range(m):
                    flag[k]=0
                break
        if circle:
            break
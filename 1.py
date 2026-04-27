q=0;act=0;seq=[];output=""
q=int(input())
for i in range(q):
    act=input().split()
    if(act[0]=="1"):
        seq.append(int(act[1]))
    elif(act[0]=="2"):
        seq.pop()
    elif(act[0]=="3"):
        print(seq[int(act[1])])
    elif(act[0]=="4"):
        seq.insert(int(act[1])+1,int(act[2]))
    elif(act[0]=="5"):
        seq=sorted(seq)
    elif(act[0]=="6"):
        seq=sorted(seq,reverse=True)
    elif(act[0]=="7"):
        print(len(seq))
    elif(act[0]=="8"):
        output=""
        for j in range(len(seq)-1):
            output+=str(seq[j])+" "
        output+=str(seq[-1])
        print(output)
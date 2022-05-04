def solve():
    a=str(input())
    b=str(input())
    n=len(a)
    m2=len(b)
    ind=0
    c=""
    d=""
    while a[ind]!='(' and ind<n:
        c+=(a[ind])
        ind+=1
    
    ind=0
    
    while b[ind]!='(' and ind<m2:
        d+=(b[ind])
        ind+=1
    
    ind+=1
    
    # print(c)
    # print(d)
    if c!=d:
        print("Predicates don't match")
    else:
        l=[]
        k=[]
        m=[]
        mp={}
        mp1={}
        for i in range(ind,n-1):
            if a[i]!=',':
                k.append(a[i])
                if a[i] in mp:
                    mp[a[i]]+=1
                else:
                    mp[a[i]]=1
                
        for i in range(ind,m2-1):
            if b[i]!=',':
                m.append(b[i])
                if b[i] in mp1:
                    mp1[b[i]]+=1
                else:
                    mp1[b[i]]=1
        
        # print(k)
        # print(m)
        k1=list(set(k))
        m1=list(set(m))  
        if len(k1)!=len(m1):
            print("Number of aruments are different")
        else:
            pl=[]
            n1=len(k)
            for i in range(0,n1):
                x=mp[k[i]]
                y=mp1[m[i]]
                if x==y:
                    if k[i]!=m[i] and (k[i],m[i]) not in pl:
                        pl.append((k[i],m[i]))
                    else:
                        pl.append(k[i])
            
            g=len(pl)
            for i in range(0,g):
                if len(pl[i])>1:
                    print('{',pl[i][0],'/',pl[i][1],'}',end=" ")
                else:
                    print('{',pl[i],'}',end=" ")
                if i!=g-1:
                    print(", ",end="")

t = 1
while t:
    solve()
    t -= 1
    

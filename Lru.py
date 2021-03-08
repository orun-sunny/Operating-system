#page mapping (LRU)

a=[]
sum=0
f= int (input("Enter no of Frames: "))
check= input("Do you want to use user input[y/n]: ")
if check=='y':
    a=[7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1]
    print("Inputs are: ", a)
else:
    n= int (input("Enter no of String : "))
    print("Enter the string: ")
    for i in range(n):
      t= int (input())
      a.append(t)
n=len(a)
m=[]
c=[]
t=[]
total=0
idx=0
for i in range(f):
    m.append(-1)
    t.append(0)

print('\nOutput wil be: ')
for i in range(n):
    test=0
    for p in range(f):
        c.append(m[p])

    for j in range(f):
        if a[i]==m[j]:
            test=1
            total+=1
            t[j]=total
            break
    if test==0:
        idx=t.index(min(t))
        m[idx]= a[i]
        total+=1
        t[idx]=total
        sum+=1


    if c==m:
        for q in range(f):
            print('-',end=' ')
    else:
        for q in range(f):
            if m[q]==-1:
                print("-",end=' ')
            else:
                print(m[q],end=' ')
    c.clear()
    print()

print("Page Fault: ",sum)
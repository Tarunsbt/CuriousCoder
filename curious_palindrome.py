def rev(a):
    
    s=0
    e=len(a)-1
    while s<e:
        a[s],a[e]=a[e],a[s]
        s+=1
        e-=1
    print(a)
arr=[1,2,3,4,5]
rev(arr)

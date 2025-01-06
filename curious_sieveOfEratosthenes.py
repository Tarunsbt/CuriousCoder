def sieveOfEratosthenes(N):
    	#code here 
    	a=[]
    	arr=[0]*(N+1)
    	for i in range(2,int(N**0.5)+1):
    	    if arr[i]==0:
    	        for j in range(i*2,N+1,i):
    	            arr[j]=1
    	for i in range(2,N+1):
    	    if arr[i]==0:
    	        a.append(i)
    	print(a)
sieveOfEratosthenes(20)    	

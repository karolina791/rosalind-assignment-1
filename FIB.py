def fibonacci(n,k):
    value1= 1
    value2= 1
    
    for n in range(1, n-1):
        result= (value1 + value2*k)
        value2=value1
        value1=result
 
    print (int(result))


fibonacci(30,4)
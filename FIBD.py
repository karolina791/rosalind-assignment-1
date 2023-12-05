def m_fibonacci(n, m):
    values = [1,1]
    
    for i in range (2,n):
        if (i< m) or (m==0):
            values.append(values[i-1]+ values[i-2])
            
        elif i==m:
            values.append(values[i-1]+ values[i-2]-1)
            
        else:
            values.append(values[i - 1] + values[i - 2] - values[i - (m + 1)])
            
    print  (values[-1])

       
m_fibonacci(95,20)
    

def prob_alleles(k,n):
    from math import factorial

    population= 2**k
    Psum=0
    
    for i in range (n,population+1):
        P=factorial(population)/factorial(i)/(factorial(population-i))*(0.25**i)*((0.75)**(population-i))
        Psum+=P
        
    print (round(Psum,3))
    

    
prob_alleles(5,7)


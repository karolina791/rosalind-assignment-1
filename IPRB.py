def dom_probability(x,v,z):
    p=x+v+z
    prob=(((x-1)*x)+((3/4)*((v-1)*v))+2*(x*v)+2*(x*z)+(v*z))/((p-1)*p)
    
    print (prob)
    
dom_probability(24, 19, 16)
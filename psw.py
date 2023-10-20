import random
caratteri_psw = ("q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m,1,2,3,4,5,6,7,8,9,0,!,?,-,.,_,/")

pizza = int(input("Quante lettere/numeri deve avere la tua password?"))
password = []
for i in range (pizza):
    char = random.choice(caratteri_psw)
    password.append(char)
    print (char)


 

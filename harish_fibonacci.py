n=int(input("how many terms you want to enter  ?    ")) 
n1=0 
n2=1 
count=0 

if(n<=0): 
    print("Please enter positive number !")
elif(n==1):
    print(n1) 
elif(n>0):
    print('it is fibonacci series-----')
    while(count<=n):
        print(n2,end=',')
        
        n3=n1+n2 
       
       
        n1=n2 
        n2=n3 
       
        count=count+1

      

       
      
 


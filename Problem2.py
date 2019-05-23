#By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
#find the sum of the even-valued terms.

t_1=1 # temporary term 1
t_2=1 # temporary term 2
t_3=1 # temporary term 3
r_c=0 # running sum

n= input("Find the sum of the even-valued terms in the Fibonacci sequence up to? ")

while t_3 < n:      
    t_3=t_1 +t_2    # Fibonacci sequence formula => Term_n= term(number-2) + term(number-1)
    t_1=t_2         #set temporary term one to the value of term two
    t_2=t_3         #set temporary term two to the value of term three
    if t_3 % 2 == 0:    # if even
        r_c += t_3      #add current term to running sum
        
print "The sum is " + str(r_c) #prints the sum of the even-valued terms in the Fibonacci sequence up to n
 

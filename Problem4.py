#Find the largest palindrome made from the product of two 3-digit numbers...


palindromes= [] #list of palindromes
for a in range (100,1000): #from the first 3 digit integer to 999, the last
   for b in range (100,1000): #from the first 3 digit integer to 999, the last
     num = str(a*b).split() [0] #multiple of a and b into string, splits each chracter of the product,orders the charcters [0 through 2], reverse is [-3 through -1]
     if len(num) ==6:
             if num[0]==num[-1] and num[1]==num[-2] and num[2]== num[-3]: #if its a pallindrome...
                palindromes.append(a*b) #add the product to the list 


print max(palindromes) #prints the  biggest number in the list
    
                          
####google, github, and youtube were very helpful recources in the making of this####

#find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20..

n=1 # the running number, takes a long while...
x=11        #checks starting at 11, 11-20 have multiples of 1-10 so we dont need to double check for divisability
while 1>0: #while True
   print n  #prints n, why? to watch it, it takes a while...
   if n%x == 0:
      x+=1     #adds one divisability checker
      if x==20:
         break
   else:
      n+=1     #add one o n
      x=11     #sets it back to 11 if n isn't divisable by x at any point
print "The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is " + str(n)


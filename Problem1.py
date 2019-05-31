#Question #1 ######## multiples of three and five ##########
#This program prints the multiples of three and five in order up to n
#it also finds the sum
three_total= 3
five_total= 5
r_s=0 #running sum 
last_added=0

n= input("Multiples of 3 and 5 up to? ")

#this loop prints the multiple of three and five in order,while simultaniously adding the multiples to a running sum it also makes sure the numbers are printed
#the last_added varable was added to avoid double counted nmultiples 
while three_total <= n and five_total <= n : 
  if three_total<= five_total:  #makes sure smallest number printed first
      if last_added != three_total: # makes sure double counting doesn't happen
        print three_total
        r_s += three_total          
        last_added = three_total 
      three_total += 3
  else:
    if last_added != five_total:
      print five_total
      r_s += five_total
      last_added = five_total
    five_total += 5

print "the sum = " + str(r_s) 

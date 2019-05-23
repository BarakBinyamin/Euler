#question #1 ######## multiples of three and five ##########
#this prints multiples of three and five in order up to n
#it also finds the sum
three_total= 3
five_total= 5
r_s=0 #running sum 
last_added=0

n= input("Multiples of 3 and 5 up to? ")

while three_total <= n and five_total <= n : #makes sure smallest # printed first
  if three_total<= five_total:
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

print "the sum = " + str(r_s) #prints the sum

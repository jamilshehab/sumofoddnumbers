#trying my best to explain the code 

#declare a variable called user number 
user_number=int(input("enter the user number:"))
#assign total to zero 
total=0
#perform a loop through the user input
for number in range(1,user_number):
    #if the number of remainder 2 is not equal to zero 
    if number % 2!=0:
       #calculate the total according to the number increment
       total+=number
#print the total of the odd numbers
print("the sum of the provided odd number is : " , total)

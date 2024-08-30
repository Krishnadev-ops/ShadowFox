'''
Write a function that takes two arguments, 145 and 'o'
,and uses the `format` function to return a formatted string.
Print the result. Try to identify the representation used
'''
def format(num,char):
    return "{} {}".format(num,char)

print(format(145,'o'))

#When you run this code, it will output:
#  145 o


#------------------------------------------------------------------------------------
# 2.  In a village, there is a circular pond with a radius of 84 meters. 
# Calculate the area of the pond using the formula: Circle Area = π r^2. (Use the value 3.14 for π) 
# Bonus Question: If there is exactly 1.4 liters of water in a square meter, what is the total amount of water in the pond? 
# Print the answer without any decimal point in it. Hint: Circle Area = π r^2 Water in the pond = Pond Area Water per Square Meter

radius= 84
pi= 3.14

pond_area= int((pi* radius*radius))
pond_water=int((pond_area*1.4))

print(f"total pond area is={pond_area}")
print(f"total water in pond={pond_water}")

#the otput will be
# total pond area is=22155
# total water in pond=31016

#-------------------------------------------------------------

# 3. If you cross a 490 meter long street in 7 minutes, calculate your speed in meters per second. 
#    Print the answer without any decimal point in it. Hint: Speed = Distance / Time

distance=490
time=7 
speed= int((distance/time)) #formula of speed calc
print(f"the speed ={speed}")

#the ans will be 70






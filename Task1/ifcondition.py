'''
1. Write a program to determine the BMI Category based on user input. Ask the user to:
Enter height in meters
Enter weight in kilograms
Calculate BMI using the formula: BMI = weight / (height)2
Use the following categories:
If BMI is 30 or greater, print "Obesity"
If BMI is between 25 and 29, print "Overweight"
If BMI is between 18.5 and 25, print "Normal"
If BMI is less than 18.5, print "Underweight"
Example:
Enter height in meters: 1.75
Enter weight in kilograms: 70
Output: "Normal"
'''

def bmi():
    height=float(input("enter height in meters:"))
    weight=float(input("enter your weight in kilogram:"))
    BMI = (weight/(height*2))                 # Calculating BMI 

    # Start of If Else ladder
     
    if BMI >= 30 :                                 
        print("Obesity")
    elif BMI > 25 and BMI <= 29 :       
        print("Overweight")
    elif BMI > 18.5 and BMI <= 25 :     
        print("Normal")
    elif BMI < 18.5 :                   
        print("Underweight")
    else :
        print ("Wrong Input")           # Wrong Input 

bmi()                   # Calling Funtion 

#------------------------------------------------------------

# 2. Write a program to determine which country a city belongs to. Given list of cities per country:
# Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
# UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
# India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
# Ask the user to enter a city name and print the corresponding country.
# Example:
# Enter a city name: "Abu Dhabi" 
# Output: "Abu Dhabi is in UAE"

Australia = ["sydney", "melbourne", "brisbane", "perth"]
UAE = ["dubai", "abu dhabi", "sharjah", "ajman"]
India = ["mumbai", "bangalore", "chennai", "delhi"]

city=input("city name:")
city_name = city.lower()

#if else loop start

if city_name in Australia:
    print(f"{city_name} is in australia")
elif city_name  in UAE:
    print (f"{city_name} is in UAE")
elif city_name in India:
    print (f"{city_name}is in india")
else:
    print("no info")
#-------------------------------------------------------------------------------------
# 3. Write a program to check if two cities belong to the same country. 
# Ask the user to enter two cities and print whether they belong to the same country or not.
# Example:
# Enter the first city: "Mumbai"
# Enter the second city: "Chennai"
# Output: "Both cities are in India"
# Example:
# Enter the first city: "Sydney"
# Enter the second city: "Dubai"
# Output: "They don't belong to the same country"
# '''
city1_name=input("1st city name:") 
city2_name=input("2nd city name")
city1_name = city1_name.lower()
city2_name = city2_name.lower()

#if else loop start
if city1_name in Australia and city2_name in Australia:
    print(f"{city1_name} and {city2_name} are in austrlia")
elif city1_name in UAE and city2_name in UAE :                         # Checking if the city names comes under the UAE List
    print("Both cities are in UAE")
elif city1_name in India and city2_name in India :                     # Checking if the city names comes under the India List
    print ("Both cities are in India")
else :
    print ("They don't belong to the same country")      # Wrong Input Handling





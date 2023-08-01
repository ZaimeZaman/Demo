#Q.4: Write a program in python to input your age in years
#Convert the age in months,days,hours,minutes and seconds 
#and then print all these values on the screen...

print("\n\n\t***This is the age convertor into mm/dd/h/m/s***\n\n")
#These all variables are initialize per year
months=12
days=365
hours=8760
min=525600
sec=31536000
a=int(input("Enter your age :"))
print(f" 1. You are {a*months} months old.")
print(f" 2. You are {a*days} days old.")
print(f" 3. You are {a*hours} hours old.")
print(f" 4. You are {a*min} minutes old.")
print(f" 5. You are {a*sec} seconds old.")
print("\n\t***THANKS***\n\n")
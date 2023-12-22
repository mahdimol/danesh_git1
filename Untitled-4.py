num1 = float(input("Enter the grade of the first lesson :"))
num2 = float(input("Enter the grade of the second lesson :"))
num3 = float(input("Enter the grade of the third lesson :"))
num4 = float(input("Enter the grade of the fourth lesson :"))
num5 = float(input("Enter the grade of the fifth lesson :"))
# Sum of course grades 
s =num1+num2+num3+num4+num5 
# average =avr
avr= s/5

if num1 > 20 :
    print('invalid Grade')   
elif num2 >  20 :
    print('invalid Grade')    
elif num3 >  20 :
    print('invalid Grade')    
elif num4 >  20 :
    print('invalid Grade')    
elif num5 >  20 :
    print('invalid Grade')
else :
    if avr >= 0 and avr <= 11.99 :
        print("F")
    elif avr > 12 and avr <= 14.99 :
        print("C")
    elif avr > 15 and avr <= 17.99 :
        print("B")
    elif avr > 18 and avr <= 20  :
        print("A")
    else:
        print("The number is not in any of the specified ranges")


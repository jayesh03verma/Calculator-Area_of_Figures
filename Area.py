#what we need
#Sum, subtarct, multiply, divide, modulus
#two numbers
#Radius, lengh and base for Area's

import math as M
        
def SUM(a,b):
    return a+b

def SUBTRACT(a,b):
    return a-b

def MULTIPLY(a,b):
    return a*b

def DIVIDE(a,b):
    return a/b

def MODULUS(a,b):
    return a%b
    
def Area_Of_Circle(a): 
    return M.pi*a*a
    
def Area_Of_Triangle(a,b):
    return 0.5*a*b
    
def Continue():
    cont = input("Wanna do more calculations ? Y/N\n")
    if cont == "n" or cont == "N":
        return False
    else:
        return True    
    
while True:
        print('Select which operation you want to perform:' '\n'
        '1. Addition\n'
        '2. Subtraction \n'
        '3. Multiplication \n'
        '4. Division \n'
        '5. Modulus \n'
        '6. Area of Circle \n'
        '7. Area of Triangle \n')           
        
        
        select = int(input('Opt an option  from 1, 2, 3, 4, 5, 6, 7:\n'))
        
        if select < 6:
            #INPUT is Used to get an input from user and if selection is less than 6
         a = float(input('Enter your first number:'))  
         b = float(input('Enter your second number:'))
         
            #Selection equls to 6
        elif select == 6:
             a = float(input('Enter the radius of circle:'))
             
            #Selection equals to 7
        elif select == 7:
             a = float(input('Enter the base length of triangle:'))     
             b = float(input('Enter the height length of triangle:'))  
        else:
            print("Out of range option you selected")
            
            #On the basis of input selection operations are happening
        if select == 1:
            print(a, "+", b, "=", SUM(a,b))
        
        elif select == 2:
            print(a, "-", b, "=", SUBTRACT(a,b))  
        
        elif select == 3:
            print(a, "*", b, "=", MULTIPLY(a,b))
        
        elif select == 4:
            print(a, "/", b, "=", DIVIDE(a,b)) 
            
        elif select == 5:
            print(a, "%", b, "=", MODULUS(a,b))       
        
        elif select == 6:
            print('Area of circle having radius' + " ", a, ":", Area_Of_Circle(a))
            
        elif select == 7:
            print('Area of Traingle having Base length' + "=", a, "and height length" + "=", b, ":", Area_Of_Triangle(a,b))
            
        else: 
            print("Invalid input")    
        if not Continue():
            break


  
# Name: Yi Mao
# Prog Purpose: This program finds the cost of movie tickets 
# Price for one ticket: $10.99
# Sales tax rate: 5.5%

import datetime

################ define global varables ###############
SMALL = 9.99
MEDIUM = 12.99
LARGE = 14.99
EX_LARGE = 17.99
TAX = 0.055

# define global variables 
size = 'S'
num = 0
size2 = 'S'
num2 = 0
size3 = 'S'
num3 = 0
size4 = 'S'
num4 = 0
pizza1_cost = 0
pizza2_cost = 0
pizza3_cost = 0
pizza4_cost = 0
total_pizza_cost = 0 
sales_tax = 0
total = 0


############### define program functions ##################
def main():
    get_user_data()
    perform_calculations()
    display_results()
    print("Thank you for your order.")

def get_user_data():
    global size ,num, size2, num2, size3,num3,size4,num4
    size = str(input(" Please enter:\n 1.'S' for Small\n 2. 'M for Medium\n 3.'L' for Large \n 4. 'XL' for Extra large\n What size of pizza would you like to order?"))
    print (size)
    num = int(input("Number of pizza: "))
    yesno = input("\nDo you want to order more?(Y/N):")
    if yesno == "Y" or yesno == "y":
        size2 = str(input(" Please enter:\n 1.'S' for Small\n 2. 'M for Medium\n 3.'L' for Large \n 4. 'XL' for Extra large\n What size of pizza would you like to order?"))
        num2 = int(input("Number of pizza: "))
    else: 
        return
    yesno = input("\nDo you want to order more?(Y/N):")
    if yesno == "Y" or yesno == "y":
        size2 = str(input(" Please enter:\n 1.'S' for Small\n 2. 'M for Medium\n 3.'L' for Large \n 4. 'XL' for Extra large\n What size of pizza would you like to order?"))
        num2 = int(input("Number of pizza: "))
    else: 
        return
    yesno = input("\nDo you want to order more?(Y/N):")
    if yesno == "Y" or yesno == "y":
        size3 = str(input(" Please enter:\n 1.'S' for Small\n 2. 'M for Medium\n 3.'L' for Large \n 4. 'XL' for Extra large\n What size of pizza would you like to order?"))
        num3 = int(input("Number of pizza: "))
    else: 
        return

    yesno = input("\nDo you want to order more?(Y/N):")
    if yesno == "Y" or yesno == "y":
        size4 = str(input(" Please enter:\n 1.'S' for Small\n 2. 'M for Medium\n 3.'L' for Large \n 4. 'XL' for Extra large\n What size of pizza would you like to order?"))
        num4 = int(input("Number of pizza: "))
    else: 
        return
    
        

def perform_calculations():
    global pizza1_cost, pizza2_cost,pizza3_cost,pizza4_cost, total, total_pizza_cost, sales_tax
    if size == 'S' or size == 's':
        pizza1_cost = num* SMALL
    elif size == 'M' or size == 'm':
        pizza1_cost = num*MEDIUM
    elif size == 'L' or size == 'l':
        pizza1_cost = num*LARGE
    elif size == 'XL' or size == 'xl':
        pizza1_cost = num*EX_LARGE

    if size2 == 'S' or size2 == 's':
        pizza2_cost = num2*SMALL
    elif size2 == 'M' or size2 == 'm':
        pizza2_cost = num2*MEDIUM
    elif size2 == 'L' or size2 == 'l':
        pizza2_cost = num2*LARGE
    elif size2 == 'XL' or size2 == 'xl':
        pizza2_cost = num2*EX_LARGE

    if size3 == 'S' or size3 == 's':
        pizza3_cost = num3*SMALL
    elif size3 == 'M' or size3 == 'm':
        pizza3_cost = num3*MEDIUM
    elif size3 == 'L' or size3 == 'l':
        pizza3_cost = num3*LARGE
    elif size3 == 'XL' or size3 == 'xl':
        pizza3_cost = num3*EX_LARGE

    if size4 == 'S' or size4 == 's':
        pizza4_cost = num4*SMALL
    elif size4 == 'M' or size4 == 'm':
        pizza4_cost = num4*MEDIUM
    elif size4 == 'L' or size4 == 'l':
        pizza4_cost = num4*LARGE
    elif size4 == 'XL' or size4 == 'xl':
        pizza4_cost = num4*EX_LARGE    
    
    total_pizza_cost = pizza1_cost + pizza2_cost + pizza3_cost +pizza4_cost
    sales_tax = total_pizza_cost*TAX
    total = total_pizza_cost + sales_tax

def display_results():
    dashes = '-------------------------------'
    print(dashes)
    print('****** Palermo Pizza ******')
    print('Your neighborhood pizzeria!')
    print(dashes)
    if size == 'S' or size == 's':
        print ('Size of Pizza   :    Small') 
    elif size == 'M' or size == 'm':
        print ('Size of Pizza   :    Medium') 
    elif size == 'L' or size == 'l':
        print ('Size of Pizza   :    Large') 
    elif size == 'XL' or size == 'xl':
        print ('Size of Pizza   :    Extra Large') 
    print('Number of Pizza ' + str(num))
    print('Cost of Pizza(s)' + format(pizza1_cost,'10,.2f'))
    print(dashes)
    if pizza2_cost != 0: 
        if size2 == 'S' or size2 =='s':
            print ('Size of Pizza   :    Small') 
        elif size2 == 'M' or size2 == 'm':
            print ('Size of Pizza   :    Medium') 
        elif size == 'L' or size2 == 'l':
            print ('Size of Pizza   :    Large') 
        elif size == 'XL' or size2 == 'xl':
            print ('Size of Pizza   :    Extra Large') 
        print('Number of Pizza ' + str(num2))
        print('Cost of Pizza(s)' + format(pizza2_cost,'10,.2f'))
        print(dashes)
    if pizza3_cost != 0: 
        if size3 == 'S' or size3 == 's':
            print ('Size of Pizza   :    Small') 
        elif size3 == 'M' or size3 == 'm':
            print ('Size of Pizza   :    Medium') 
        elif size3 == 'L' or size3 == 'l':
            print ('Size of Pizza   :    Large') 
        elif size3 == 'XL' or size3 == 'xl':
            print ('Size of Pizza   :    Extra Large') 
        print('Number of Pizza ' + str(num3))
        print('Cost of Pizza(s)' + format(pizza3_cost,'10,.2f'))
        print(dashes)
    if pizza4_cost != 0: 
        if size4 == 'S' or size4 == 's':
            print ('Size of Pizza   :    Small') 
        elif size4 == 'M' or size4 == 'm':
            print ('Size of Pizza   :    Medium') 
        elif size4 == 'L' or size4 == 'l':
            print ('Size of Pizza   :    Large') 
        elif size4 == 'XL' or size4 == 'xl':
            print ('Size of Pizza   :    Extra Large') 
        print('Number of Pizza ' + str(num4))
        print('Cost of Pizza(s)' + format(pizza4_cost,'10,.2f'))
        print(dashes)

    print('Balance Owed  :' +  format(total,'10,.2f'))
    print(dashes)
    print(str(datetime.datetime.now()))

############# Call on main program to execute ###############
main()



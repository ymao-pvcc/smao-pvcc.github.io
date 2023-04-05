# Name: Yi Mao
# Prog Purpose: 
# Progan Essential Elements 
# 

import datetime

################ define global varables ###############
CASHIER = 16.50
STOCKER = 15.75
JANITOR = 15.75
MAINTENANCE = 19.50

################ define global varables ###############
FEDTAXR = 0.12
STATAXR = 0.03
SSTAXR = 0.062
MEDICARE = 0.0145

# define global variables 
grosspay = 0
fedtax = 0
statax = 0
sstax = 0
medtax = 0
deduc = 0
job = 'C'
hours = 0
netpay = 0

############### define program functions ##################
def main():
    more_data= True
    while more_data:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\n would you like to input data for another employee?(Y/N):")
        if yesno == "n" or yesno == "N":
            more_data == False
            print("Thank you for using our app.")

def get_user_data():
    global job, hours
    job = input("Category Code: (Please enter 'C' for cashier, 'S' for Stocker, 'J' for Janitor, 'M' for Maintenance)")
    hours = int(input("Number of hours worked: "))

def perform_calculations():
    global grosspay, fedtax,statax,sstax,medtax,deduc,netpay
    if job == 'C' or job == 'c':
        grosspay = hours * CASHIER
    elif job == 'S' or job == 'S':
        grosspay = hours * STOCKER
    elif job == 'J' or job == 'j':
        grosspay = hours * JANITOR
    elif job == 'M' or job == 'm':
        grosspay = hours * MAINTENANCE
    fedtax = FEDTAXR * grosspay
    statax = STATAXR * grosspay
    sstax = SSTAXR * grosspay
    medtax = MEDICARE * grosspay
    deduc = fedtax + statax + sstax + medtax
    netpay = grosspay - deduc

    
    

def display_results():
    dashes = '--------------------------------------------'
    print(dashes)
    print('******** Program Essential Elements *******')
    print(dashes)
    print('************** Deduction Tax **************')
    print('Federal income tax       $ ' + format(fedtax,'8,.2f'))
    print('State income tax         $ ' + format(statax,'8,.2f'))
    print('Social Security tax      $ ' + format(sstax,'8,.2f'))
    print('Medicare tax             $ ' + format(medtax,'8,.2f'))
    print('Total Deduction          $ ' + format(deduc,'8,.2f'))
    print('******************* Pay *******************')
    print('Gross Pay          $ ' + format(grosspay,'8,.2f'))
    print('Net Pay            $ ' + format(netpay,'8,.2f'))
    print(dashes)
    print(str(datetime.datetime.now()))

############# Call on main program to execute ###############
main()



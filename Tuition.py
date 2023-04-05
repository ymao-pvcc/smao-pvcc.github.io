# Name: Yi Mao
# Prog Purpose: This program finds the cost of movie tickets 
# Price for one ticket: $10.99
# Sales tax rate: 5.5%

import datetime

################ define global varables ###############
TUITION_IN = 155
TUITION_OUT = 331.6
INST_FEE = 1.75
STU_ACT_FEE = 2.90
CAP = 23.5

# define global variables 
num_credits= 0
total = 0
scholar_amt = 0
balance = 0
residency = 1

############### define program functions ##################
def main():
    more_data= True
    while more_data:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nDo you want to process more data?(Y/N):")
        if yesno == "n" or yesno == "N":
            more_data == False
            print("Thank you for using our app.")

def get_user_data():
    global residency, num_credits, scholar_amt
    residency = int(input("Residency status:\nEnter: 1 for in-state; 2 for Out-of State:"))
    num_credits = int(input("Number of credits: "))
    scholar_amt = int(input("Amount of scholarship awarded: "))

def perform_calculations():
    global tuition_amt, inst_amt, act_amt,cap_amt,total,balance
    if residency == 2:
        tuition_amt = num_credits*TUITION_OUT
        cap_amt = num_credits * CAP
    else:
        tuition_amt = num_credits*TUITION_IN
        cap_amt = 0

    inst_amt = num_credits*INST_FEE
    act_amt = num_credits*STU_ACT_FEE
    total = tuition_amt+inst_amt+act_amt+cap_amt
    balance = total - scholar_amt

def display_results():
    dashes = '-------------------------------'
    print(dashes)
    print('**** Piedmont Virginia Commnity College ****')
    print('Your neighborhood movie house')
    print(dashes)
    print('Number of Credits: ' + str(num_credits))
    print(dashes)
    print('Tuition             $ ' +  format(tuition_amt,'10,.2f'))
    print('Capital Fee         $ ' +  format(cap_amt,'10,.2f'))
    print('Institution Fee     $ ' +  format(inst_amt,'10,.2f'))
    print('Activitiy Fee       $ ' +  format(act_amt,'10,.2f'))
    print('Total               $ ' +  format(total,'10,.2f'))
    print('Scholarship         $ ' +  format(scholar_amt,'10,.2f'))
    print(dashes)
    print('Balance Owed ' +  format(balance,'10,.2f'))
    print(dashes)
    print(str(datetime.datetime.now()))
    print("NOTE:PVCC Fee Rates: https://www.pvcc.edu/tuitionandfees")

############# Call on main program to execute ###############
main()



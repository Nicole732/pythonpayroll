#!/usr/bin/env python3
#ACME Corporation needs a simple payroll program written in Python.
#The Input: Employee Name, Hours worked, Pay Rate (hourly)
#Employees are to receive 1.5x pay rate for hours over 40
#Fed Tax = 10%, State tax = 3%,FICA rate = 7%
#Output: Name Hours Rate Grosspay Fed Tax State Tax FICA Netpay
#** Bonus:  Can the program process multiple employees inputs before program ends?


#Fed Tax = 10%, State tax = 3%,FICA rate = 7%, Overtime = 1.5xpay rate
fedTaxRate = 0.1
stateTaxRate = 0.03
ficaTaxRate = 0.07
overTimeRate = 1.5

#initialize employee lists to store employee data
#empInfoList = []
emp1InfoList= []
emp2InfoList=[]
emp3InfoList=[]
#initialise employee list dictionary
allEmpList = []

# Define various functions 
#Input information
def inputData(x):
    empName = str(input("Enter Employee Name: ")) #trim??
    hoursWorked = int(input("Enter the numbers of hours worked: "))
    payRate = int(input("Enter the hourly pay rate: $"))
    # store employee info in empList
    x.insert(0,empName)
    x.insert(1,hoursWorked)
    x.insert(2,payRate)
    return x

#function grossPay calculates the employee grosspay for a given employee
# grosspay = (hourly rate x hours worked ) + (Overtime h. x overtimerate X hourly rate)
def grossPay(x):
    #Calculate Overtime hours 
    overTimeHours = x[1] - 40

    #calculate GrossPay
    if x[1] > 40:
        grossP = ((x[2] * (x[1] - overTimeHours)) + (x[2] * overTimeHours * overTimeRate))
    else:
        grossP = x[2] * x[1]

    #add grossP to empInfoList
    x.insert(3,round(grossP))
    return x[3]

#function empDeductions calculates all deductions
def deductions(x):
    
    empFedTax = x[3]*fedTaxRate
    empStateTax =  x[3]*stateTaxRate
    empFICA= x[3]*ficaTaxRate
    x.insert(4,round(empFedTax))
    x.insert(5,round(empStateTax))
    x.insert(6,round(empFICA))
    totalDeduction = empFedTax + empStateTax + empFICA
    return totalDeduction

#function Netpay calculates the employee net pay
# netpay = grosspay - deductions
def netPay(x,y):
    netP = x - y
    return netP

#function to print employee info
def printOutPut(x):
    for i in range(len(x)):
        print( str(x[i]) + "\t\t", end='')
    return 

#Main 
#Header Info
print('************************************************\n')
print("Welcome to ACMEPayroll")
print("You are using ACME Corporation Payroll Program \n")
print('************************************************\n')

###### display oneEMployee info
#inputData(empInfoList)
#grossPay(empInfoList)
#print(empInfoList)
#totalD = deductions(empInfoList)
#print(empInfoList)
#empInfoList.append(round(netPay(empInfoList[3],totalD)))
#print(empInfoList)
#printOutPut(empInfoList)
#print('\n')

######several employees - (2)
inputData(emp1InfoList)
grossPay(emp1InfoList)
totalD = deductions(emp1InfoList)
emp1InfoList.append(round(netPay(emp1InfoList[3],totalD)))
print('\n')

inputData(emp2InfoList)
grossPay(emp2InfoList)
totalD = deductions(emp2InfoList)
emp2InfoList.append(round(netPay(emp2InfoList[3],totalD)))
print('\n')

inputData(emp3InfoList)
grossPay(emp3InfoList)
totalD = deductions(emp3InfoList)
emp3InfoList.append(round(netPay(emp3InfoList[3],totalD)))
print('\n')


print('View all the employee(s) Payroll information:')
print('***********************************************************************************************************************\n')
print("Name\tHours Worked\tpayRate($)\tgrossPay($)\tFed. Tax($)\tState Tax($)\tFICA($)\t\tNet Salary($)")
print('***********************************************************************************************************************\n')

printOutPut(emp1InfoList)
print("\n")
printOutPut(emp2InfoList)
print("\n")
printOutPut(emp3InfoList)
print("\n")
 
#DRY code
empNum = int(input("How many employees do you want to display? :  "))
print(empNum)


#input data for each employee and
for j in range(empNum):
    empInfoList=[] #re-intialises a new list for each employee
    inputData(empInfoList) #collect initial data
    grossPay(empInfoList) #caculate grosspay
    totalD = deductions(empInfoList) #calculate deductions
    empInfoList.append(round(netPay(empInfoList[3],totalD)))
    print(empInfoList)
    allEmpList.insert(j,empInfoList) #saves employee info in main list at index j   
    print(allEmpList)
#output information
print(allEmpList)
print('View all the employee(s) Payroll information:')
print('***********************************************************************************************************************\n')
print("Name\tHours Worked\tpayRate($)\tgrossPay($)\tFed. Tax($)\tState Tax($)\tFICA($)\t\tNet Salary($)")
print('***********************************************************************************************************************\n')
for j in range(empNum):
    printOutPut(allEmpList[j])
    print('\n')


# Program to calculate billing system

# Author: Amrita Sharma

billing='''Sunway int'l Electricity Billing System
           Maitidevi, Kathmandu
--------*---------*--------*----------
            '''
cus_name=input("Enter your name")
cus_address=input("Enter your address")
unit=int(input("Enter the total unit consumed"))
print(billing)
print(f'Hello {cus_name}, {cus_address}')
amount=0;
if(unit<=100):
    print("No charge")
elif(unit>100 and unit<=200):
    amount=(unit-100)*5
    print(f'Total amount: {amount:0.2f}')
elif(unit>200 and unit<=500):
    amount=500+((unit-200)*10)
    print(f'Total amount: {amount:0.2f}')
elif(unit>500):
    amount=500+((unit-400)*10)
    total=(amount*15)/100
    after_discount=amount-total
    print(f'Total amount: {after_discount:0.2f}')
else:
    print("Thank you")









def initial_Display():
    billing='''Sunway int'l Electricity Billing System
                         Maitidevi, Kathmandu
                --------*---------*--------*----------
            '''
    print(billing)

def input_Information():
    cus_name=input("Enter your name:")
    cus_address=input("Enter your address:")
    unit=int(input("Enter the total unit consumed:"))
    return cus_name,cus_address,unit

amount = 0

def calculation_Unit(unit):
    if(unit<=20):
        amount=unit*4
    elif(unit>20 and unit<=50):
        amount=unit*4+(unit-20)*7.5
    elif(unit>50 and unit<=150):
        amount=(unit-50)*9.5 + 20*4 +30*7.5
        total=(unit-50)+100*9.5*0.05
        after_discount=amount-total
    elif(unit>150 and unit<=250):
        amount=(unit-150)*11.5 + 20*4 + 30*7.5 + 100*9.5
        total=(unit-150)*11.5*0.10
        after_discount=amount-total
    elif (unit > 250):
        amount =(unit - 150) * 13.5 + 20*4 + 30*7.5 + 100*9.5 +100*11.5
        total = (unit-150)+200*11.5*0.15
        after_discount = amount - total

    else:
        print("Thank you")

    return amount,total,after_discount



initial_Display()
cus_name,cus_address,unit=input_Information()
amount,total,after_discount=calculation_Unit(unit)


print(f"Customer name : {cus_name}/t Customer address: {cus_address}")



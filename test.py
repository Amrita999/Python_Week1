import datetime

def initial_display():
    today = datetime.datetime.now()
    display=f'''
    Sunway Bhatbhateni Store
      Maitidevi, Kathmandu
                    Date: {today}
    ----------------------*------
    '''
    print(display)


def print_bill( **kwargs ):
    today = datetime.datetime.now()
    display = f"""
    \t \t **********   Sunway Bhatbhateni billing  ************
                            Maitidevi, Kathmandu
                                    Date: {today}
                        ----------------------*------
    
    
    Customer id : {kwargs['cust_id']} \t Customer Address : {kwargs['cust_address']}
    Customer Phone : {kwargs['cust_email']}
    
    Total Price : {kwargs['total_price']} \t Discounted : {kwargs['discount']}
    After Discount : {kwargs['after_discount']}
    """

    print(display)
    filename = kwargs['cust_id']+'.txt'
    f = open(filename, "w")
    f.write(display)
    f.close()




def calculation(total_price):
    if(total_price<=500):
        discount=total_price*0.05
        after_discount=total_price-discount
    elif total_price>5000 and total_price<=7000:
        discount=5000*0.5+(total_price-5000)*0.08
        after_discount=total_price-discount
    elif total_price>7000 and total_price<=10000:
        discount=5000*0.05+2000*0.08+(total_price-7000)*0.10
        after_discount=total_price-discount
    else:
        discount=5000*0.05+2000*0.08+3000*0.10+(total_price-10000)
        after_discount=total_price-discount

    return discount, after_discount


def take_item_details( **kwargs ):
    number_of_items = int(input('Enter number of items: '))

    total_price = 0

    for i in range(1, number_of_items+1):
        quantity = int(input(f"Quantity of item [{i}]"))
        unit_price = int(input(f"unit price of item [{i}]"))
        total_price += quantity*unit_price
        discount, after_discount = calculation(total_price=total_price)
    print_bill(**kwargs, discount=discount, after_discount=after_discount, total_price = total_price)
    print('*'*100)




def take_customer_details(customer_number):
    cust_id = input(f"Enter the id [{customer_number}]: ")
    cust_name = input(f"Enter the name [{customer_number}]: ")
    cust_address = input(f"Enter the address [{customer_number}]: ")
    cust_email = input(f"Enter the email address [{customer_number}]: ")

    take_item_details(customer_number=customer_number, cust_id=cust_id, cust_name=cust_name, cust_address=cust_address, cust_email=cust_email)




def main():
    initial_display()
    number_of_customers = int(input('Enter the numbers of customers: ')) # 3
    for i in range(1, number_of_customers+1):
        take_customer_details(i)
   

main()
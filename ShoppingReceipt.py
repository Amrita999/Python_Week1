# def initial_display():
#     display='''
#     Sunway Bhatbhateni Store
#       Maitidevi, Kathmandu
#                     Date:
#     ------*--------*--------*------
#     '''
#     print(display)
#
#
# initial_display()
# def cust_information():
#     cust_no=int(input("Enter the total number of customer"))
#     for i in range(cust_no):
#         cust_id=int(input(f"Enter the id [{i+1}]: "))
#         cust_name=input(f"Enter the name [{i+1}]: ")
#         cust_address=input(f"Enter the address [{i+1}]: ")
#         cust_email=input(f"Enter the email address [{i+1}]: ")
#         item_no=int(input(f"Enter the total item purchased [{i+1}]: "))
#         total_price=0
#         for j in range(item_no):
#             quantity=int(input(f"Quantity of item [{j+1}]"))
#             unit_price=int(input(f"unit price of item [{j+1}]"))
#             total_price +=total_price*unit_price
#
#     discount,after_discount=calculation(total_price)
#     initial_display()
#     output_information(cust_id,cust_name,cust_address,cust_email,discount,after_discount,total_price)
#
#
#
# def calculation(total_price):
#     if(total_price<=500):
#         discount=total_price*0.05
#         after_discount=total_price-discount
#     elif total_price>5000 and total_price<=7000:
#         discount=5000*0.5+(total_price-5000)*0.08
#         after_discount=total_price-discount
#     elif total_price>7000 and total_price<=10000:
#         discount=5000*0.05+2000*0.08+(total_price-7000)*0.10
#         after_discount=total_price-discount
#     else:
#         discount=5000*0.05+2000*0.08+3000*0.10+(total_price-10000)
#         after_discount=total_price-discount
#
#     return discount,after_discount
#
#
# def output_information(cust_id,cust_name,cust_address,cust_email,discount,after_discount,total_price):
#     initial_display()
#     print(f"customer id: {cust_id}/t/t customer name: {cust_name}")
#     print(f"customer adddress: {cust_address}/t/t customer email: {cust_email}")
#     print(f"Total price: {total_price}")
#     print(f"Discount: {discount}")
#     print(f"After discount: {after_discount}")





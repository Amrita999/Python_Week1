def Display_Static_Info():
    display = '''
\t\tSunway College Account Department
\t\t\tMaitiDevi, Kathmandu
\t\t\t\tWelcome to
\t\tSalary& Tax Calculate System (STCS)'''
    print(display)


Display_Static_Info()



def calculation_of_tax(staff_salary, status):
    if (flag):
        def Calculate_Tax_Of_Staff_Unmarried(staff_salary):
            if staff_salary <= 400000:
                tax_rate = staff_salary * 0.01
                after_tax = staff_salary + tax_rate
            elif staff_salary > 400000 and staff_salary <= 500000:
                tax_rate = (400000 * 0.01) + (staff_salary - 400000) * 0.10
                after_tax = staff_salary + tax_rate
            elif staff_salary > 500000 and staff_salary <= 700000:
                tax_rate = (400000 * 0.01) + (100000 * 0.10) + (staff_salary - 500000) * 0.20
                after_tax = staff_salary + tax_rate
            elif staff_salary > 700000 and staff_salary <= 1300000:
                tax_rate = (400000 * 0.01) + (100000 * 0.10) + (200000 * 0.20) + (staff_salary - 700000) * 0.30
                after_tax = staff_salary + tax_rate
            else:
                tax_rate = (400000 * 0.01) + (100000 * 0.10) + (200000 * 0.20) + (600000 * 0.30) + (
                        staff_salary - 1300000) * 0.36
                after_tax = staff_salary + tax_rate

            return tax_rate
    else:
        def Calculate_Tax_Of_Staff_Married(staff_salary):
            if staff_salary <= 450000:
                tax_rate = staff_salary * 0.01
                after_tax = staff_salary + tax_rate
            elif staff_salary > 450000 and staff_salary <= 550000:
                tax_rate = (450000 * 0.01) + (staff_salary - 450000) * 0.10
                after_tax = staff_salary + tax_rate
            elif staff_salary > 550000 and staff_salary <= 750000:
                tax_rate = (450000 * 0.01) + (100000 * 0.10) + (staff_salary - 550000) * 0.20
                after_tax = staff_salary + tax_rate
            elif staff_salary > 750000 and staff_salary <= 1300000:
                tax_rate = (450000 * 0.01) + (100000 * 0.10) + (200000 * 0.20) + (staff_salary - 750000) * 0.30
                after_tax = staff_salary + tax_rate
            else:
                tax_rate = (450000 * 0.01) + (100000 * 0.10) + (200000 * 0.20) + (550000 * 0.30) + (
                        staff_salary - 1300000) * 0.36
                after_tax = staff_salary + tax_rate

            return tax_rate

def Display_Staff_Info(staff_name, staff_address, staff_pan_no, staff_fiscal_year, staff_status,tax_rate):
    print(f"Staff Name: {staff_name}\t\t Address: {staff_address}")
    print(f"PAN NO: {staff_pan_no}\t FY: {staff_fiscal_year}\t Marital Status: {staff_status}")

    print(f"Staff {staff_name} with {staff_pan_no} fall under (----) Tax salb. ")
    print(f"{staff_name} ({staff_pan_no}) to pay tax to government is Rs = {tax_rate} ")


staff_no = int(input("Please enter the number of staff you wanted you provide data: "))
list_staff = []
flag = False

def Staff_Info(staff_no,tax_rate):
    for i in range(staff_no):
        information = []
        staff_name = input(f"Enter staff name [{i + 1}]: ")
        information.append(staff_name)
        staff_address = input(f"Enter staff address [{i + 1}]: ")
        information.append(staff_address)
        staff_pan_no = int(input(f"Enter staff PAN number [{i + 1}] : "))
        information.append(staff_pan_no)
        staff_status = input(f"Enter 'Y' for Married and 'N' for Unmarried [{i + 1}]: ").upper()
        if staff_status == "Y":
            flag = True
        information.append(staff_status)

        staff_fiscal_year = int(input(f"Enter Fiscal Year[{i + 1}]:  "))
        information.append(staff_fiscal_year)
        staff_salary = int(input(f"Enter staff per month income Rs. [{i + 1}]"))
        information.append(staff_salary)
        list_staff.append(information)
        calculation_of_tax(staff_salary, staff_status)
        Display_Static_Info()
        Display_Staff_Info(staff_name, staff_address, staff_pan_no, staff_fiscal_year, staff_status,tax_rate)
        print(list_staff)


Staff_Info(staff_no,tax_rate)

initial_dis ='''
            WELCOME TO SUNWAY CHARACTER CHECK SYSTEM
                    MAITIDEVI, KATHMANDU
            -------*-------*------*----------*-----
            '''
print(initial_dis)
string_input= input("Enter the string for character check")
low_count, up_count, spec_char, num_data = 0, 0, 0, 0
for i in range(len(string_input)):
    if (string_input[i]>='A' and string_input[i] <= 'Z'):
        up_count+=1
    elif (string_input[i] >= '0' and string_input[i] <= '9'):
        num_data += 1
    elif (string_input[i] >= 'a' and string_input[i] <= 'z'):
        low_count += 1
    else:
        spec_char += 1
print(initial_dis)
print(f"UpperCase:{up_count}")
print(f"Numeric data: {num_data}")
print(f"LowerCase: {low_count}")
print(f"Special_char: {spec_char}")
print("Thank You For Your Visit")
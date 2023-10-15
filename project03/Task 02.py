# create the program to find valid phone number
phone_no = str(input("Enter your 10 digit phone number : "))

if len(phone_no) == 10 and phone_no.isdigit():
    print("valid phone number")
else:
    print("invalid phone number")

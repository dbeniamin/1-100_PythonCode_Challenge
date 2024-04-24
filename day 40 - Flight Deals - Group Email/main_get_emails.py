import sheety

print("Welcome to Benjamin's Flight Club. \n \
      You will get the best flight deals by email !!")

first_name = input("What is your first name ? ..").title()
last_name = input("What is your last name ? ..").title()

email1 = "email1"
email2 = "email2"

while email1 != email2:
    email1 = input("What is your email? ")
    if email1.lower() == "quit" \
            or email1.lower() == "exit":
        exit()

    email2 = input("Please confirm your Email !.")
    if email2.lower() == "quit" \
            or email2.lower() == "exit":
        exit()

print("Welcome to Flight Club")

sheety.post_new_row(first_name, last_name, email1)

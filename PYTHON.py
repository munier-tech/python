
# i = 0

# while  i < 100:
#   if i % 2 == 0:
#      print(i)
#   i += 1
     



# # number = 8

# # while number >= 0 :
# #   if number % 2 == 0 : 
# #     print("even number")
# #   else:
# #     print("odd number")



# while True:
#         print("\n--- Calculator Menu ---")
#         print("1. Addition (+)")
#         print("2. Subtraction (-)")
#         print("3. Multiplication (*)")
#         print("4. Division (/)")
#         print("5. Modulus (%)")
#         print("6. Exit")

#         choice = input("Choose an operation (1-6): ")
        
#         if choice == '6':
#             print("Exiting calculator. Goodbye!")
#             break

#         if choice not in ['1', '2', '3', '4', '5']:
#             print("Invalid choice. Please select a valid option.")
#             continue

#         if choice == float : 
#             break

#         if choice == '1' : 
#             print(input("enter a number 1 "))
#             print(input("enter a number 2 "))
        
#         if choice == '2' : 
#             print(input("enter a number 1 "))
#             print(input("enter a number 2 "))
#             print(input("enter a number 3 "))

#         if choice == '3' : 
#             print(input("enter a number 1 "))
#             print(input("enter a number 2 "))
#             print(input("enter a number 3 "))
#             print(input("enter a number 4 "))
             
#         if choice == '4' : 
#             print(input("enter a number 1 "))
#             print(input("enter a number 2 "))

#         if choice == "5" : 
#             print(input("enter a number 1 "))
        
#         if choice == "6" :

#            break
       


#  question 1

def personal_info():
    birth_year = int(input("Enter your birth year: "))
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    age = 2025 - birth_year
    return f"Dear {first_name} {last_name}, you are {age} years old."

print(personal_info())

# question 2  


def math_operations():
  
    num1 = float(input("Enter a number: "))
    num2 = float(input("Enter number : "))

  
    int_num1 = int(num1)
    int_num2 = int(num2)

    print(f"\nConverted numbers to integers: {int_num1}, {int_num2}\n")

  
    print(f"Addition: {int_num1} + {int_num2} = {int_num1 + int_num2}")
    print(f"Subtraction: {int_num1} - {int_num2} = {int_num1 - int_num2}")
    print(f"Multiplication: {int_num1} * {int_num2} = {int_num1 * int_num2}")
    

    
    
    

# Run the program
math_operations()



def check_even_odd():
   
    num = int(input("Enter an integer: "))
    if num % 2 == 0:
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")

# Run the program
check_even_odd()

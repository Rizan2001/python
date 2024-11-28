# try:
#     numerator = 10
#     denominator = 0

#     result = numerator/denominator

#     print(result)
# except:
#     print("error:denominator cannot be 0.")

#     try:

#         even_numbers = [2,4,6,8]
#         print(even_numbers[5])
#     except IndexError:
#         print("index out of bound.")

# try: 
#     num = int(input("enter a number: "))
# except ValueError:
#     print("that is not a valid number!")
# else:
#     print(f"you enterd the number:(num)")
# finally:
#     print("execusion complete.")

try:
    lets = (input("enter a letter: "))
except ValueError:
    print("it is not a letter!")
else:
    print(f"you entered the letter:(lets)")
finally:
    print("execusion complete.") 
    


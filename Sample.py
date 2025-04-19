# a = "String,Test" 
# b = a.split("t")
# print(b)
# # print(" Type of B:", type(b))
# # print(a.replace(" ","-"))
# if len(b)==2:
#     print("Length is 2")
# else:
#     print("Length less than 2")


# 13%1=1
# 13%2=1
# 13%3=1
# 13%4=1
# 13&5=3
# odd_num_list = [1,3,5,7,9,11,15]
# #check number is even or odd
# if num1%2==0: # modulus 
#     print("Number is even")
# else:
#     print("Number is odd")
#check number is prime 
#1,3,5,7,11,13,17,19,23,29,31
# if num1%2==1:
#     print("Number is prime")
# else:
#     print("Number is not prime")   
# function definition - def  - a logic which takes input and returns output 

# num1 = input("Enter number:")
# int_num = int(num1)
# def is_prime(num):
#     if num <= 1:
#         print("number is not prime")
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 return False
#         return True
# #function calling
# print(f"Number {int_num} is prime: {is_prime(int_num)}")

# a = int(input("Enter number 1:"))
# b = int(input("Enter number 2:"))
# c = int(input("Enter number 3:"))
# if a>b and a>c:
#     print("Number 1 is greater")
# elif b>a and b>c:
#     print("Number 2 is greater")
# else:
#     print("Number 3 is greater")
# ❎
# list_of_playing = ["Rohit Sharma","Rickleton", "Tilak Varma", "Suryakumar","Hardik Pandya"]
# final_size_of_playing_XI = 11
# for i in range(final_size_of_playing_XI-len(list_of_playing)):
#     a = input(f"Enter player number {i+6}: ")
#     list_of_playing.append(a)
# impact_player_list=[]
# impact_player_size = 5
# for i in range(impact_player_size):
#     a = input(f"Enter impact player number {i+1}: ")
#     impact_player_list.append(a)
#dictionary of final player who will be on ground
# match_info ={
#     "Playing XI players list":list_of_playing,
#     "Impact Player list":impact_player_list,
#     "Umpire name":["Richard K","Nitin Menon"],
#     "Match Venue":"Wankhede Stadium",
#     "Match Start time": "7:30 Pm",
#     "Match Number": 32,
#     "Broadcasting channel":"Jio Hotstar"
# }
match_info = {
    "Playing XI players list": [
        "Rohit Sharma",
        "Rickleton",
        "Tilak Varma",
        "Suryakumar",
        "Hardik Pandya",
        "Will jacks",
        "Mitchell Santner",
        "Jasprit Bumrah",
        "Deepak Chahar",
        "Trent Bout",
        "Karn Sharma"
    ],
    "Impact Player list": [
        "Vignesh Puthur","Aswini Kumar",
        "Bevon Jacobs",
        "Robin Minz",
        "Naman Dhir"
    ],
    "Umpire name": [
        "Richard K",
        "Nitin Menon"
    ],
    "Match Venue": "Wankhede Stadium",
    "Match Start time": "7:30 Pm",
    "Match Number": 32,
    "Broadcasting channel": "Jio Hotstar"
}


# a = ["abcd","achd","abcd","abdc","cadb","dbac"]
# new_list = []
# for i in a:
#     if i not in new_list:
#         new_list.append(i)

# my_list = [10, 20, 30]
# my_list[1] = 99  # Modifying element
# print(my_list)

# my_tuple = (10, 20, 30)
# my_tuple[1] = 99  # ❌ This will raise an error!

person_info ={
     "Person Name":"Dhairya",
    "Age":18,
    "Gender":"Male",
    "Phone no":"8756478936",
    "Address": "Bhayandar west",
 }

a = input("Enter person Info that you want to know: ")
print(person_info[a])
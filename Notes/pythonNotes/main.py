from pythonDemo1 import get_user_info
userID =int( input("Enter the userId : "))
user = get_user_info(userID)

for keys in user:
    print (keys)



option = input("what info of user you need? ")
user_data = user.get(option)

if user_data == None:
    print("No user data found..")

else:
    print(user_data)

import requests

def get_user_info(id):
    request = requests.get("https://jsonplaceholder.typicode.com/users/"+str(id))
    json = request.json()
    user_name = json.get("username")
    user_email = json.get("email")
    user_city = json.get("address").get("city")
    return {
        'username': user_name,
        'email': user_email,
        'city': user_city
            }


user = get_user_info(3)
print(user)
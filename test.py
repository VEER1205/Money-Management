import requests

# Correcting the way the login_id is passed
log = {
  "username": "veer",
  "password": "1"
}
uid = requests.post(f"http://127.0.0.1:8000/login",json=log).json()
data = requests.get(f"http://127.0.0.1:8000/load_data/{uid}").json()
print(type(uid))  # Should print the user ID if login is successful, otherwise "Login failed"
print(data)  # Should print the user data loaded from the server
 # Should print the JSON response from the server

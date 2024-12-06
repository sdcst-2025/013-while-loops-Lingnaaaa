#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:

username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied

example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 12345
Access granted


"""
username =""
password =""

while username!='admin' or password !='12345':
    username = input('Enter your username:')
    password = input('Enter your password:')
    if username!='admin' or password !='12345':
        print('Access denied')
    if username == "admin" and password == "12345":
        print('Access granted')
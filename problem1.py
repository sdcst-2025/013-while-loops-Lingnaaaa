##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied

example:
example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 1234
Access denied
Too many failed attempts. Access denied.
"""
username=""
password=""

maxtime=2
time=0
while (username!='admin' or password!="12345") and time<=maxtime:
    username=input("username:")
    password=input("password:")
    time+=1
    print('Access denied')
    if username=='admin' and password=="12345" and time<=maxtime:
        print("Access granted")
    if time>maxtime:
        print('Too many failed attempts. Access denied.')


#write a python script develop one meaningful usecase using logical OR operator?


import time
print()
print('==============FACEBOOK=============')
print()
print('======Enter you Login Details======')
print('-----------------------------------')
print()
id=input('Enter your user ID or mobile number:')
password1=input('Enter password:  ')
password2=input('Enter confirm password:  ')
print()
if (id=="leela0006" or id=="1234567890" and password1=="Leela@2099" and password2=="Leela@2099"):
    print('✅✅Login Sucessfull✅✅')
    print()
    print('Enjoy your FACEBOOK')
else:
    print('❌❌❌❌❌Invalid Details please enter correct Details❌❌❌❌❌')
print()
time.sleep(2)
print('End of an applications')
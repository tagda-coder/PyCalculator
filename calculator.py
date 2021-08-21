#!/usr/bin/env python
"""Hey Guys From This Python Script You can Do Following Task Like :-

 Addition 
 Subtraction 
 Multiplication   ]: Coded by Mandeep :[
 Division

 As A Basic Calculator.....

 Well You Can Enhance The features of This Dtool But Give Us Credit ..

 """

# Code Start From Here okay 
# You can Contact me Learn making tool okay 
# Contact me from this Number :- +919939411504

# ------------------------------ # 

# Import OS Module
import os 
os.system("clear") # This Line will clear the screen 

print("\033[33m\033[1mHello User")
print("\033[1m\033[33mThis is A Calculator and It can Perform Basic Tasks.  \033[42m ]:\033[37m Coded By \033[43m\033[31mMandeep \033[32m:[ \033[0m")
print("\033[1m\033[31m\033[4m............................\033[0m")
print()
num1 = int(input("\033[1m\033[33m[\033[32m!\033[33m]\033[34m Enter the First Number : \033[32m"))
num2 = int(input("\033[1m\033[33m[\033[32m!\033[33m]\033[34m Enter the Second Number : \033[32m"))

print("\033[4m............................")
print()

# Addition Line 

print("\033[32m[\033[33m1\033[32m]\033[31m\033[4m Addition")
print("\033[32m[\033[33m2\033[32m]\033[31m\033[4m Subtraction")
print("\033[32m[\033[33m3\033[32m]\033[31m\033[4m MultiPlication")
print("\033[32m[\033[33m4\033[32m]\033[31m\033[4m Division")
print()
opt = int(input("\033[31m➢ \033[32mEnter your Choice : \033[31m"))


# Condition for The User:- 

# If_Else Condition 


if opt == 1:
    Ans = num1 + num2
    print()
    print("\033[31mAnswer:-\033[32m", Ans)

elif opt == 2:
    Ans = num1-num2
    print()
    print("\033[31mAnswer:-\033[32m", Ans)

elif opt == 3:
    Ans = num1*num2
    print()
    print("\033[31mAnswer:-\033[32m", Ans)
elif opt == 4:
    Ans = num1%num2
    Ans2 = num1/num2
    print("\033[32m")
    print("\033[31mRemainder:- \033[33m",Ans)
    print("\033[31mQuotient:- \033[33m",Ans2)
    print()

    
else :
    print("\033[33m\033[1mYou Press Invalid Option !")



            

















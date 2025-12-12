'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import random
import math 
 
t=int(input("Enter your upper :"))
n=int(input("Enter your lower :"))
z=random.randint(n,t)
s=math.ceil(math.log(t-n+1,2))
print("Your have %d changes to guess!"%(s))
i=1
while i<=s:
     print("Enter your guess:")
     d=int(input())
     if d==z:
         print("you guessed correctly in %d chance"%(i))
         break;
     elif d>z:
         print("you guessed high")
     else :
         print("you guessed low")
     i+=1
     if i==s:
         print("You lost your guess chance")

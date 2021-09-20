#paper,stone,scissior
import random

c=int(0)
y=int(0)

def gamei(comp,you):
    if(comp == you):
        return 1
    elif(comp == 'p'):
        if(you == 's'):
            return 3
        elif(you == 'x'):
            return 2
    elif(comp == 's'):
        if(you == 'p'):
            return 2
        elif(you == 'x'):
            return 3
    elif(comp == 'x'):
        if(you == 'p'):
            return 3
        elif(you == 's'):
            return 2
    
n = int(input("How many rounds you want to play? "))  

for i in range(1,n+1):  
    
 rand = random.randint(1,3)
 if rand == 1:
    comp = 'p'
 elif rand == 2:
    comp = 's'
 elif rand == 3:
    comp = 'x'

 print("***** Round No.", i,"*****\n")

 you = input('''Please enter your choice?
 * for paper - p
 * for stone - s
 * for scissior - x
 Enter your response - ''')

 

 a = gamei(comp,you)
 if a == 1:
    print("\n*****It's a Draw!*****")
    print("\nComputer Response "+comp)
    print("Your Response "+you) 
    print("\n") 
    
 elif a == 2:
    print("\n*****You Won!*****")
    print("Computer Response "+comp)
    print("Your Response "+you)
    print("\n")
    
    y = y+1
 elif a==3:
    print("\n*****Computer won!*****")
    print("Computer Response "+comp)
    print("Your Response "+you)
    print("\n")
    
    c = c+1
    

if y>c:
    print("Final Result - You won!\n")
    print("*****Score*****")
    print("Computer ",c, "You",y)

elif y==c:
    print("Final Result - Draw!\n")
    print("*****Score*****")
    print("Computer ",c, "You",y)
elif y<c:
    print("Final Result - Computer won!\n")
    print("*****Score*****")
    print("Computer ",c, "You",y)
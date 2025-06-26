import random
n=random.randint(1,100)
a=-1
guesses=0
while(a!=n) :
    a=int(input("Enter the number:"))
    if(a>n) :
        print("Lower number please")
        guesses+=1
    elif(n>a):
        print("Higher number please")
        guesses+=1
print(f"You have guesses the number {n} corectly in {guesses} attempts")

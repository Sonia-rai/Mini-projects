# guess the name game



import random
print("\t\t\t\t\t\t\t\t\t\tWELCOME TO GUESS THE NUMBER GAME\n")
print("RULES ARE SIMPLE:\n1.CHOOSE RANGE i.e LOWER AND UPPER LIMIT\n2.YOU WILL HAVE 5 ATTEMPTS ONLY")


try:
     a=int(input("Enter the lower limit:"))
     b=int(input("Enter the upper limit:"))
     num=random.randint(a,b)
     ctr=0

     while ctr<5:
        guess=int(input(f"Guess the number between {a} and {b} :"))
        if  a<=guess<=b:
           if guess==num:
              print("CONGRAS!! YOU WIN")
              break

           elif guess<num:
               print("THE GUESSED NUMBER IS LESS!! ENTER BIGGER NUMBER ")
               ctr+=1

           elif guess>num:
                print("THE GUESSED NUMBER IS HIGH!! GUESS SMALLER NUMBER ")
                ctr+=1
        else:
            print("ENTER NUMBER WITHIN LIMITS")
     else:
          print("YOU LOSE!! THE NUMBER WAS",num)

except ValueError:
    print("PLEASE ENTER VALID INPUT i.e INTEGER")


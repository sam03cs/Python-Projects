from multiprocessing.sharedctypes import Value


print("Hello! Welcome to Sam's Python Calculator.")
print()
while True:
    try:
        val1, val2 = input("Enter two values:").split()
    except ValueError:
        print("Please enter two values...")
        continue
#int(val1)
#int(val2)
#print(val1,val2)
    print("Would you like to Add(a), Subtract(s), Multiply(m), or Divide(d)? Enter Below:")
    op = input().lower()
    try:
        if op == 'a':
            add = int(val1) + int(val2)
            print("Okay! {} + {} is {}".format(val1,val2,add))    
        elif op == 's':
            sub = int(val1) - int(val2)
            print("Great! {} - {} is {}".format(val1,val2,sub))
        elif op == 'm':
            mult = int(val1) * int(val2)
            print("Awesome! {} * {} is {}".format(val1,val2,mult))   
        elif op == 'd':
            div = int(val1) / int(val2)
            print("Cool! {} / {} is {}".format(val1,val2,div))
        elif op != 'a' or 's' or 'm' or 'd':
            print("Sorry! Please enter one of the letters above.")
            pass
    except ValueError:
            print("Please enter valid numbers.")
        
    
    if input('Do you wish to continue?:').lower() == 'y' or \
        input('Do you wish to continue?:').lower().startswith('y'):
        continue
    elif input('Do you wish to continue?:').lower() == 'n' or \
    input('Do you wish to continue?:').lower().startswith('no'):
        print("Goodbye!")
        break
   
    #else:
        #print("Please type either yes(y) or no(n)")

#now on github


#ADD FUNCTION THAT ASKS THE USER IF THEY ARE DONE, IF NO LOOP AGAIN IF YES QUIT
      
   

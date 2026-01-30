
prompt = "what is your name?"
name= input(prompt)

try:
    prompt2 = "how old are you?" + name + "?"
    age = input(prompt2)

    age = int(age)
    print("you were born in,", 2025-age)
    print("nice knowing you")


except ValueError:
    print("sorry," , name, "but that is not a number")
except NameError:
    print("sorry that is not a valid name for print")
except:
    print("all other exceptions go here!")
else:
    print("Thanks for playin fair")
finally:
    print("this is always at the end no matter what")








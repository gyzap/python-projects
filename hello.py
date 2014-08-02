print("welcome")

name = input("who r u ?")
name = name.strip().title()

if name == 'Luke':
    print("hi luke")
elif name == "Patrick":
    print("go home")
elif name == 'Godzilla':
    print('how is tokyo and america for ya, ' + name)
elif name == 'Pinky Pie':
    print('when is the next party')
else:
    print("hi "+ name)
          
print("good bye")

feeling = input("how are you feeling?")
print("you are feeling " + feeling + ". i feel like that too")

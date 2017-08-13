# This program says hello and asks for your name and age
print('Hello stranger')
print('What is your name?') # ask for their name
UserName=input()
print ('It is good to meet you, '+ UserName)
print('The length of your name is:')
print ((str(len(UserName))) + str(' characters'))
print('What is your age?') # ask for their age
UserAge=input()
print ('You will be ' +str(int(UserAge)+1) +' in a year.')

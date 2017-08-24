# This program says hello and asks for your name and age
print('Üdv, idegen!')
print('Mi a becses neved?') # ask for their name
UserName=input()
print('Örülök, hogy megismerhetlek '+ UserName)
print('Neved hosszúsága:')
print((str(len(UserName))) + str(' betű'))
print('Mennyi idős vagy?') # ask for their age
UserAge=input()
print('Képzeld ' +str(int(UserAge)+1) +' éves leszel egy év múlva! :P')

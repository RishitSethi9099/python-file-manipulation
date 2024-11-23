f= open('story.txt','r')
reading= f.read()
print(reading)
vowel= 0
consonant= 0
lowercase= 0
uppercase= 0
space= 0
for i in reading:
    if i in 'aeiouAEIOU':
        vowel+=1
    else:
        consonant+=1
    if i.islower():
        lowercase+=1
    elif i.isupper():
        uppercase+=1
    else:
        space+=1
print(f'vowel: {vowel}')
print(f'consonant: {consonant}')
print(f'lowercase: {lowercase}')
print(f'uppercase: {uppercase}')
print(f'space: {space}')

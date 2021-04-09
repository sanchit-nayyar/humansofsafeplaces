import os

os.system('pip install instaloader word_forms nltk pytest matplotlib')
get_word_forms('hello')
os.system('touch suggested_hashtags.txt')
os.system('touch story.txt')
f = open('securityInfo.json')
username = str(input('Enter Instagram Username: '))
password = str(input('Enter Instagram Password (Will be visible in plain text while entering): '))
f.write('{\n\t"Username": "' + username + '",\n\t"Password": "' + password + '"\n}')
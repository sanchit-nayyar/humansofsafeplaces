f = open('story.txt')
words = f.read().replace('\n', ' ')
while '  ' in words:
	words = words.replace('  ', ' ')
words = words.split(' ')

from word_forms.word_forms import get_word_forms

import json
secInfo = open('securityInfo.json').read()
t = json.loads(secInfo)
print()

baseList = []

for word in words:
	D = get_word_forms(word)
	for k in D:
		for i in D[k]:
			if "'" not in i and '"' not in i:
				baseList.append(i.replace(' ', '_'))

baseSet = set(baseList)

print(set(baseList))

from instaloader import Instaloader, Hashtag

tagName = 'bull'

L = Instaloader()
L.login(t['Username'], t['Password'])


M = {}

g = len(baseSet)
cm = 1

f = open('backup.csv')

existingSet = [i.split(',')[0] for i in f.read()[:-1].split('\n')]
existingValues = [i.split(',')[1] for i in f.read()[:-1].split('\n')]

f.close()

f.open('backup.csv', 'a')

for tagName in baseSet:
	print(tagName, "Analysing - ", cm, "/", g)
	cm += 1
	n = -1
	try:
		n = existingSet.index(tagName)
		M[tagName] = existingValues[n]
	except ValueError:
		print('Tag not found in backup. Fetching information from Instagram')
	if n == -1:
		try:
			tag = Hashtag.from_name(L.context, tagName)
			M[tagName] = tag.mediacount
			f.write(tagName + "," + str(M[tagName]) + '\n')
		except:
			print('Hashtag not found in Instagram')
			f.write(tagName + ",-1\n")
# print([i.name for i in tag.get_related_tags()])

f.close()

M2 = sorted(M.items(), key=lambda x: x[1])


c = 0
for i in M2:
	c += 1
	if c > 10:
		break
	print(i)
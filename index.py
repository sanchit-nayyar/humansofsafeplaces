from instaloader import Instaloader, Hashtag
from word_forms.word_forms import get_word_forms
import matplotlib.pyplot as plt
import json, sys, os

f = open('story.txt')
words = f.read().replace('\n', ' ').replace(',', '')
f.close()
while '  ' in words:
	words = words.replace('  ', ' ')
words = words.split(' ')

f = open('suggested_hashtags.txt')
suggested_hashtags = set(f.read().split('\n'))
f.close()


secInfo = open('securityInfo.json').read()
t = json.loads(secInfo)

baseList = []

for word in words:
	D = get_word_forms(word)
	baseList.append(word)
	for k in D:
		for i in D[k]:
			if "'" not in i and '"' not in i:
				baseList.append(i.replace(' ', '_'))

baseSet = set(baseList)

print(set(baseList))

L = Instaloader()
L.login(t['Username'], t['Password'])

M = {}

g = len(baseSet)
cm = 1

if not os.path.exists('backup.csv'):
	os.system('touch backup.csv')

f = open('backup.csv')
fCont = f.read()

existingSet = [i.split(',')[0] for i in fCont[:-1].split('\n')]
existingValues = [i.split(',')[1] for i in fCont[:-1].split('\n')]

f.close()

f = open('backup.csv', 'a')

for tagName in baseSet:
	print(tagName, "Analysing - ", cm, "/", g)
	cm += 1
	n = -1
	try:
		n = existingSet.index(tagName)
		M[tagName] = int(existingValues[n])
	except ValueError:
		print('Tag not found in backup. Fetching information from Instagram')
	if n == -1:
		try:
			tag = Hashtag.from_name(L.context, tagName)
			M[tagName] = int(tag.mediacount)
			f.write(tagName + "," + str(M[tagName]) + '\n')
		except Exception:
			print('Hashtag not found in Instagram', str(E))
			f.write(tagName + ",-1\n")
# print([i.name for i in tag.get_related_tags()])

f.close()

M2 = sorted(M.items(), key=lambda x: x[1], reverse = True)


c = 0
for i in M2:
	if i not in suggested_hashtags:
		c += 1
		if c > int(sys.argv[1]):
			break
		print(i)

HashtagList = list(suggested_hashtags)
HashtagPosts = []

f = open('backup.csv', 'a')

for tag in HashtagList:
	n = -1
	try:
		n = existingSet.index(tag)
		HashtagPosts.append(int(existingValues[n]))
	except ValueError:
		print('Tag not found in backup. Fetching information from Instagram')
	if n == -1:
		try:
			tagX = Hashtag.from_name(L.context, tag)
			HashtagPosts.append(int(tagX.mediacount))
			f.write(tag + "," + str(HashtagPosts[-1]) + '\n')
		except:
			HashtagPosts.append(0)
			f.write(tag + ",-1\n")


plt.bar(HashtagList, HashtagPosts)
plt.title('Hashtag Trend Analysis')
plt.xlabel('Tag Name')
plt.ylabel('Reach Metric')
plt.show()
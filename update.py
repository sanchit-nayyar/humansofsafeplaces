from instaloader import Instaloader, Hashtag
import sys, os

k = 0
if len(sys.argv) > 1:
	k = sys.argv[1]

if k not in [0, 1, 2]:
	k = 0

f = open('backup.csv')
hashtagset = f.read().split('\n')[:-1]
f.close()

f = open('backup.csv', 'w')

secInfo = open('securityInfo.json').read()
t = json.loads(secInfo)

L = Instaloader()
L.login(t['Username'], t['Password'])

for row in hashtagset:
	hashtagdesc = row.split(',')
	hashtagname = hashtagdesc[0]
	hashtagcnt = hashtagdesc[1]
	if k in [1, 2] and hashtagcnt != '-1':
		hashtagcnt = Hashtag.from_name(L.context, hashtagname)
	if k in [0, 2] and hashtagcnt == '-1':
		hashtagcnt = Hashtag.from_name(L.context, hashtagname)

	f.write(hashtagname + ',' + hashtagcnt + '\n')

f.close()
print("Update Process completed.")
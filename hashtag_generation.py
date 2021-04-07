from instaloader import Instaloader, Hashtag

tagName = 'bull'

L = Instaloader()
L.login('<<username>>', '<<password>>')
tag = Hashtag.from_name(L.context, tagName)
# print(tag.mediacount)
# print([i.name for i in tag.get_related_tags()])

for i in tag.get_related_tags():
	print(1)
	print(i)
	exit()
import pytchat
#If you need better data control use Youtubes Live Data API v3 
chat = pytchat.create(video_id="jfKfPfyJRdk")
allowed = ["b", 'a', 'u', 'd', 'l', 'r', 's', 'x', 'y']
msg = ""

while chat.is_alive():
	f = open("Run.txt", "a")
	for c in chat.get().sync_items():
		print(c.message)
		commands = ""
		for letter in c.message:
			if letter in allowed:
				msg += letter
	f.write(msg)
	print(f'commands passed: {msg}')
	msg = ""
	f.close()

import subprocess
while True:
	subprocess.run(" npx cowsay -r --think I wish I was...",shell=True)
	if input("Show one more cow?") != 'y':
		break

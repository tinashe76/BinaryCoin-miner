def verify(x):
	import hashlib
	
	if 0.5 >= x >= 0.1:
		dust = hashlib.sha1(b'Option 1')
		pixie_dust = dust.hexdigest()
		return pixie_dust

	elif 1 >= x >= 0.6:
		dust = hashlib.sha1(b'Option 2')
		pixie_dust = dust.hexdigest()
		return pixie_dust

	elif x < 0.1:
		dust = hashlib.sha1(b'Option 3')
		pixie_dust = dust.hexdigest()
		return pixie_dust

	elif x > 1:
		dust = hashlib.sha1(b'Option 4')
		pixie_dust = dust.hexdigest()
		return pixie_dust


# ***************************************************************************************************************************************
def save(x, y): #Code is not yet working
	def verify(x):
		if 0.5 >= x >= 0.1:
			import hashlib
			dust = hashlib.sha1(b'Option 1')
			pixie_dust = dust.hexdigest()
			return pixie_dust

		elif 1 >= x >= 0.6:
			import hashlib
			dust = hashlib.sha1(b'Option 2')
			pixie_dust = dust.hexdigest()
			return pixie_dust

		elif x < 0.1:
			import hashlib
			dust = hashlib.sha1(b'Option 3')
			pixie_dust = dust.hexdigest()
			return pixie_dust

		elif x > 1:
			import hashlib
			dust = hashlib.sha1(b'Option 4')
			pixie_dust = dust.hexdigest()
			return pixie_dust

	save_file = open("save.txt", "w")
	save_file.write(f"ZW DOLLAR: ${x}              |             Withdraw Code: {watcher.verify(y)}")
	save_file.close()
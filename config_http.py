class Config:

	def __init__(self):
		None

	def header(self):
		try:
			config = open('config_httppmine')
		except:
			print "configuration file [ config_httppmine ] not found"
			exit(0)

		header = {}
		for param in config.read().split('http_header{')[1].split('}')[0].split('\n'):

			if len(param) > 2:
				head = param.split(':')
				header[head[0]] = head[1]

		return header

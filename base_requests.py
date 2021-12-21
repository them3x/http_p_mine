import requests
import socket

class default:

	def __init__(self):
		None

	def d(self, domain, method):

		try:
			d = domain.split('://')[1].split('/')[0]
		except:
			print "correctly specify the URL [ https://domain.com/ or http://domain.com/ ]"
			exit(0)

		data = socket.gethostbyname(d)
		ip = str(repr(data)).replace("'", "")

		if method == "get":
			req = requests.get(domain)

		elif method == "post":
			req = requests.post(domain)

		http = str(req.text.encode('UTF-8'))
		status_code = req.status_code

		if status_code == "200":
			print "Ops, the page "+str(domain)+" returned a code "+str(status_code)
			exit(0)

		return ip, http, status_code

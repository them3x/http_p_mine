from datetime import date
import itertools
import hashlib
import requests
import threading
import sys, time

class mine:

	def __init__(self, wordlist, domain, method, http_original, header, ori_code):

		global done
		done = False

		file = open('config_httppmine')
		values = set()
		for value in file.read().split('http_values{')[1].split('}')[0].split('\n'):
			if len(value) >= 1:
				values.add(value)



		def animate():
			for c in itertools.cycle(['|-   |', '| -  |', '|  - |', '|   -|','|  - |','| -  |']):
				if done:
					break

			        sys.stdout.write('\r'+c)
        			sys.stdout.flush()
				time.sleep(0.1)

			sys.stdout.write('\rDone!\n')


		def other_values(values):
			date1 = date.today().strftime("%d-%m-%Y")
                        date2 = date.today().strftime("%m-%d-%Y")
			date1_md5 = hashlib.md5(date1).hexdigest()
                        date2_md5 = hashlib.md5(date2).hexdigest()

			values.add(date1_md5)
                        values.add(date2_md5)
                        values.add(date1)
                        values.add(date2)

			return values

		values = other_values(values)

		t = threading.Thread(target=animate)
		t.start()

		try:
			for word in wordlist:
				for value in values:
					if method == "get":
						url = str(domain) + "?" + str(word) + "=" + str(value)
						http = requests.get(url, headers=header)

						http_text = str(http.text.encode('UTF-8'))
						status_code = http.status_code

						if status_code != ori_code:
							print url + "\t [CODE:"+str(status_code)+"]"

						elif value in http_text and value not in http_original:
							print url + "\t [Reflected value in HTTP]"

						elif len(http_text) > int(str(len(http_original) * 0.1).split('.')[0]) + len(http_original):
							print url + "\t [different sizes] [Original:"+str(len(http_original))+"][Other:"+str(len(http_text))+"]"

	#					print "HTTP Req:",len(http_text)
	#					print "HTTP Orig:",len(http_original)
			done = True
		except Exception as erro:
			print erro
			done = True
			exit(0)

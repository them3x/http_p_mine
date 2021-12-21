import requests
import sys
import config_http
import config_wordlist
import base_requests
import param_mine

def banner(domain, ip):
        print "=======##########################=======\n########| Parameter miner HTTP |########\n=======##########################======="
        print "Domain:",domain.split('://')[1].split('/')[0]
	print "File:", domain.replace(domain.split('/')[2], "").replace('https://', "").replace('http://', "")
	print "IP:",ip
	print "=======##########################=======\n"


if len(sys.argv) < 3:
	print "Use: python",sys.argv[0], "<http://domain.com/> <method> <wordlist - optional>"
	print "Avaliable methods: -g <get>"
	exit(0)

domain = sys.argv[1]
method = sys.argv[2]

if len(sys.argv) < 4:
	wordlist = "paramns.txt"
else:
	wordlist = sys.argv[3]

header = config_http.Config().header()
wordlist = config_wordlist.wordlist().organize(wordlist)

if method == "-g":
	method = "get"
elif method == "-p":
	method = "post"
else:
	print "Option [ "+str(method)+" ] not found"
	exit(0)

ip, original_http, original_code = base_requests.default().d(domain, method)
banner(domain, ip)
param_mine.mine(wordlist,domain,  method, original_http, header, original_code)

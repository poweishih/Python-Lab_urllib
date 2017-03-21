import argparse
import os

def Request(URL):
	headers = {};
	headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17';
	
	req = urllib.request.Request(URL, data=None, headers=headers, origin_req_host=None, unverifiable=False, method=None)
	
	print(req.__dict__)
	print('=========================')
	print('Full URL: %s' % req.full_url)
	print('Type: %s' % req.type)
	print('Host: %s' % req.host)
	print('Origin request host: %s' % req.origin_req_host)
	print('Unverifiable: %s' % req.unverifiable)
	print('=========================')

	print(urllib.request.urlopen(req).headers.__dict__)

parser = argparse.ArgumentParser(description='')
parser.add_argument("-u", "--url", help="Input url. ex: http://123.123.123.123")
parser.add_argument("-f", "--function", help="request")
args = parser.parse_args()

if args.function == None or args.url == None:
	os.system("python3 urllib_request.py -h")
else:
	if args.function == 'request':
		import urllib.request
		Request(args.url)
	# filter_http(args.filename, args.url, args.count)
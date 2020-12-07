import sys,requests
try:
	urldosya = open(sys.argv[1],'r')
	urlsatirlar = urldosya.readlines()
	admindosya = open(sys.argv[2],'r')
	adminsatirlar = admindosya.readlines()
	for urls in urlsatirlar:
		url = urls.rstrip()
		for admins in adminsatirlar:
			admin = admins.rstrip()
			try:
				r = requests.get(url+admin,timeout=float(sys.argv[3]))
				if requests.get(url+"bypassec0x1337").status_code == 200:
					pass
				elif "wp-submit" in r.text.lower() and "wordpress" in r.text.lower() and r.status_code == 200:
					print(url+admin,"==> Wordpress")
				elif 'index.php?route=' in r.text.lower() and 'opencart' in r.text.lower() and r.status_code == 200:
					print(url+admin,"==> Opencart")
				elif 'joomla' in r.text.lower() and 'type="password"' in r.text.lower() and r.status_code == 200:
					print(url+admin,"==> Joomla")
				elif 'type="password"' in r.text.lower() and 'method="post"' in r.text.lower() and r.status_code == 200:
					print(url+admin)
				else:
					pass
			except:
				pass
except:
	print("Kullanimi :",sys.argv[0],"sitelist.txt adminlist.txt 10(Timeout)")

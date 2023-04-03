# coding: iso-8859-1
#!/usr/bin/env python3

from __future__ import unicode_literals
import requests
from bs4 import BeautifulSoup
import sys
from unidecode import unidecode
import time
import os
import re

while True:

	url = 'http://www.danstonchat.com'

	response = requests.get(url)

	if response.ok:
		os.system('clear')

		bashfr = '\n\n             \033[1mLES 5 DERNIÈRES QUOTES DE 🐈 DansTonChat.com 😺\033[0m\n\n'
		sys.stdout.buffer.write(bashfr.encode('iso-8859-1'))

		codehtml = BeautifulSoup(response.text, 'lxml')

		for loop in range(4, -1, -1):
			divquotesgeneral = codehtml.findAll('div', {'class': re.compile('^item item')})[loop] 
			titles = divquotesgeneral.find('h3')
			score = divquotesgeneral.find('span', {'class': 'score'})
			quotenumber = divquotesgeneral['class'][1].replace('item', '#')

			print('\n--------------------------------');
			sys.stdout.buffer.write(b'    \033[1m' + titles.text.encode('iso-8859-1') + b'\n\n\033[0m')

			try:
				quotesimg = divquotesgeneral.find('a', {'class': 'html img', 'title': True})

				if quotesimg: 
					txt = quotesimg['title'].replace('<br />', ' ')
					sys.stdout.buffer.write(txt.encode('iso-8859-1'))

				else:
					quotes = divquotesgeneral.find('div', {'class': 'item-content'})
					sys.stdout.buffer.write(quotes.text.encode('iso-8859-1'))

			except:
				print('Aucune quote ou site web inaccessible')

			print('\n\n\033[1m' + quotenumber + '\033[0m    ' + score.text + '\n--------------------------------\n\n')

	time.sleep(3600)
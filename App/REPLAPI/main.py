import requests
from bs4 import BeautifulSoup
from errors.errors import UserNotFoundError


class Client():
	def __init__(self, username):
		self.username = username
		try:
			resp = requests.get('https://replit.com/data/profiles/{}'.format(self.username))
			if resp.ok():
				self.json = resp.json()
			else:
				raise Exception
		except Exception:
			raise UserNotFoundError('User not found.')

	def bio(self):
		return self.json['bio']			
	
	def top_langs(self):
		return self.json['topLanguages']
	
	def newest_repls(self):
		return self.json['repls']
	
	


if __name__ == '__main__':
	client = Client('LAMAQDAHODWALA')
	print(client.bio())
			
import asyncio
import aiohttp
from bs4 import BeautifulSoup

class Client():
	async def __init__(self, username):
		self.username = username
		self.sess = aiohttp.ClientSession() 
		
  
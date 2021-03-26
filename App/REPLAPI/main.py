import requests, os, json, repltalk, asyncio, getpass
from bs4 import BeautifulSoup

class info(): 
  def version(self):
    print("VERSION: 0.0.3")

  def owners(self):
    print("OWNERS:\nMain Owner: JBYT27\nSide Owner(weird sidekick): darkdarcool")

class assets(): 
  async def replit_avatar_get(self, name = None):
    if (name == None):
      exit("Please fill out the name parameter!")
    else:
      try:
        client = repltalk.Client()
        user = await client.get_user(name)
        return user.avatar
      except:
        exit(f"ERROR: Cannot load {name}'s avatar!") 
  async def replit_cycle_get(self, name = None):
    if (name == None):
      exit("Please fill out the name parameter!")
    else:
      try:
        client = repltalk.Client()
        user = await client.get_user(name)
        return user.cycles
      except:
        exit(f"ERROR: Cannot load {name}'s cycles!")
  async def replit_name_get(self, name = None):
    if (name == None):
      exit("Please fill out the name parameter!")
    else:
      try:
        client = repltalk.Client()
        user = await client.get_user(name)
        return user.full_name
      except:
        exit(f"ERROR: Cannot load {name}'s name!")
  async def replit_bio_get(self, name = None):
    if (name == None):
      exit("Please fill out the name parameter!")
    else:
      try:
        client = repltalk.Client()
        user = await client.get_user(name)
        return user.bio
      except:
        exit(f"ERROR: Cannot load {name}'s bio!")
def replit_user():
    try:
      owner = os.environ['REPL_OWNER']
      return owner
    except:
      exit("ERROR: No such replit account exists!")
def replit_avatar(self, name = None):
  if (name == None):
    exit("Please fill out the name parameter!")
  else:
    try:
      e = asyncio.run(assets.replit_avatar_get(f"{name}"))
      return e
    except:
      exit(f"ERROR: Cannot find {name}'s avatar!")
def replit_bio(self, name = None):
  if (name == None):
    exit("Please fill out the name parameter!")
  else:
    try:
      e = asyncio.run(assets.replit_bio_get(f"{name}"))
      return e
    except:
      exit(f"ERROR: Cannot find {name}'s bio!")
def replit_name(self, name = None):
  if (name == None):
    exit("Please fill out the name parameter!")
  else:
    try:
      e = asyncio.run(assets.replit_name_get(f"{name}"))
      return e
    except:
      exit(f"ERROR: Cannot find {name}'s name!")
def replit_cycles(self, name = None):
    if name == None:
      exit("ERROR: You didn't fill out the name parameter!")
    else:
      try:
        e = asyncio.run(assets.replit_cycle_get(f"{name}"))
        return e
      except:
        exit("ERROR: Cannot find " + name + "'s cycles!")

def replit_langs(self, name = None):
    if name == None:
      exit("ERROR: You didn't fill out the name parameter!")
    else:
      try:
        link = requests.get('https://replit.com/data/profiles/' +name )
        data = link.json()
        #print(data)
        els = list(data.items())
        all = els[-2]
        all = list(all)
        stuff = all[1]
        stuff = str(stuff)
        stuff = stuff.replace("'", "")
        stuff = stuff.replace("[", "")
        stuff = stuff.replace("]", "")
        stuff = stuff.replace(" ", "")
        li = list(stuff.split(","))
        return (li)
      except:
        exit("ERROR: Cannot find " + name + "'s langs!")

def replit_post(self, name = None):#latest post
    if name == None:
      exit("ERROR: You didn't fill out the name parameter!")
    else:
      #user = os.environ["REPL_OWNER"]
      try:
        post = requests.get("https://replit.com/@"+ name +"?tab=posts")#name
        soup = BeautifulSoup(post.content, 'html.parser')
        html1 = soup.find("div", {"class":"jsx-2329710370 board-post-list-item-post-title"}).get_text()
        return html1
        #b = a.replace('</div>','')
        #return b
      except:
       exit("ERROR: Cannot find "+ name+"'s hottest post!")
  
def replit_posts(self, name = None):#all posts
    if name == None:
      exit("ERROR: You didn't fill out the name parameter!")
    else:
      try:
        post = requests.get("https://replit.com/@"+ name +"?tab=posts")#name
        soup = BeautifulSoup(post.content, 'html.parser')
        html1 = soup.find_all("div", {"class":"jsx-2329710370 board-post-list-item-post-title"})#.get_text()
        all_text = []
        for i in html1:
          all_text.append(i.get_text())
        return '\n'.join(all_text)
        
      except:
        exit("ERROR: Cannot find "+ name+"'s posts!")
  
def replit_comment(self, name = None):
  if name == None:
      exit("ERROR: You didn't fill out the name parameter!")
  else:
      try:
        post = requests.get("https://replit.com/@" + name + "?tab=comments")
        soup = BeautifulSoup(post.content, 'html.parser')
        for data in soup.find("p"):
          return (data.get_text())
          break # keep this here so it prints once
      except:
        exit("ERROR: Cannot find "+ name+"'s hottest comment!") 
  
def replit_comments(self, name = None):
    if name == None:
      exit("ERROR: You didn't fill out the name parameter!")
    else:
      try:
        post = requests.get("https://replit.com/@" + name + "?tab=comments")
        soup = BeautifulSoup(post.content, 'html.parser')
        all_text = []
        for data in soup.find_all("p"):
          all_text.append(data.get_text())
        return '\n'.join(all_text)
      except:
        exit("ERROR: Cannot find "+name+"'s comments!")

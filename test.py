import json
from urllib import request
import pymongo

url = "http://auction-api-us.worldofwarcraft.com/auction-data/ab1239c3bc437d48321a64e6b5e5ab7f/auctions.json"

# urllib.request.urlretrieve(url, "test.json")

req = request.urlopen(url)
data = json.loads(req.read().decode())
print(data["realms"])
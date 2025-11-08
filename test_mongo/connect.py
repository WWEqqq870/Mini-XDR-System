from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus

username = "fares"
password = quote_plus("FARES111h3X??")  # دي بتحوّل الرموز الخاصة لصيغة آمنة
uri = f"mongodb+srv://{username}:{password}@cluster0.jztcrtp.mongodb.net/?retryWrites=true&w=majority&appName=miniXDR"

client = MongoClient(uri, server_api=ServerApi('1'))
client.admin.command('ping')
print("✅ Pinged your deployment. You successfully connected to MongoDB!")



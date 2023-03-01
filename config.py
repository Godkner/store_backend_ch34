import pymongo
import certifi

con_str = "mongodb+srv://KAFA:k22042001@cluster0.9tkipgm.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("keyboards")
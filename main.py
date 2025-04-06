from pymongo import MongoClient
import gridfs

# 1. Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["image_database"]

# 2. Use GridFS
fs = gridfs.GridFS(db)

# 3. Save Image to MongoDB
with open("your_image.jpg", "rb") as image_file:
    image_id = fs.put(image_file, filename="your_image.jpg")
    print("Image saved with ID:", image_id)

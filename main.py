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
    

 # 4. Retrieve the image by filename or ID
output_data = fs.get_last_version(filename="your_image.jpg")

# 5. Save it back to disk (optional)
with open("downloaded_image.jpg", "wb") as out_file:
    out_file.write(output_data.read())
    print("Image retrieved and saved as 'downloaded_image.jpg'")


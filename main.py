from pymongo import MongoClient
import gridfs

# 1. Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["image_database"]

# 2. Use GridFS
fs = gridfs.GridFS(db)

# 3. Path to the uploaded image
image_path = "/mnt/data/papan.jpg"

# 4. Save the image to MongoDB
with open(image_path, "rb") as image_file:
    image_id = fs.put(image_file, filename="papan.jpg")
    print("✅ Image saved successfully with ID:", image_id)


# Retrieve the image from MongoDB by filename
output_data = fs.get_last_version(filename="papan.jpg")

# Save the retrieved image back to disk
with open("downloaded_papan.jpg", "wb") as out_file:
    out_file.write(output_data.read())
    print("✅ Image retrieved and saved as 'downloaded_papan.jpg'")

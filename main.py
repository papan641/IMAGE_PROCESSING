from pymongo import MongoClient
import gridfs

# Step 1: Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["image_database"]

# Step 2: Create GridFS instance
fs = gridfs.GridFS(db)

# Step 3: Path to the image
image_path = "papan.jpg"  # Make sure papan.jpg is in the same folder

# Step 4: Save the image to MongoDB
with open(image_path, "rb") as img_file:
    image_id = fs.put(img_file, filename="papan.jpg", content_type="image/jpeg")
    print(f"✅ Image uploaded successfully with ID: {image_id}")


# Step 5: Retrieve the image
output_file = fs.get_last_version(filename="papan.jpg")

# Step 6: Save to disk
with open("downloaded_papan.jpg", "wb") as f:
    f.write(output_file.read())
    print("✅ Image retrieved and saved as 'downloaded_papan.jpg'")

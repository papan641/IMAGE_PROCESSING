import cv2
import numpy as np
from pymongo import MongoClient
import gridfs

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["image_db"]
fs = gridfs.GridFS(db)

# -------- STEP 1: Read and Store Image --------
def save_image_to_db(image_path):
    # Read image using OpenCV
    img = cv2.imread(image_path)
    if img is None:
        print("❌ Image not found!")
        return

    # Convert to bytes
    _, img_encoded = cv2.imencode('.jpg', img)
    img_bytes = img_encoded.tobytes()

    # Save to MongoDB
    img_id = fs.put(img_bytes, filename="papan.jpg", content_type="image/jpeg")
    print("✅ Image saved with ID:", img_id)

# -------- STEP 2: Read Image from DB and Show --------
def show_image_from_db(filename):
    # Fetch image by filename
    output = fs.get_last_version(filename)
    image_bytes = output.read()

    # Convert to OpenCV format
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Show image
    cv2.imshow("Image from MongoDB", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ---------- MAIN ----------
if __name__ == "__main__":
    image_path = "papan.jpg"  # Make sure this file exists in the same folder
    save_image_to_db(image_path)
    show_image_from_db("papan.jpg")

// Import mongoose
const mongoose = require('mongoose');

// Connect to MongoDB
main()
  .then(() => {
    console.log("Connection successful");
  })
  .catch((err) => {
    console.log("Connection failed:", err);
  });

async function main() {
  await mongoose.connect('mongodb://127.0.0.1:27017/test');
}

// Define schema
const userSchema = new mongoose.Schema({
  name: String,
  email: String,
  age: Number,
});

// Create model
const User = mongoose.model("User", userSchema);

// Create a new user
const user2 = new User({
  name: "john",
  email: "papan@gmail.in",
  age: 20,
});

// Save to the database
user2
  .save()
  .then((res) => {
    console.log("User saved:", res); // fixed: was console.log(err) by mistake
  })
  .catch((err) => {
    console.log("Error saving user:", err);
  });

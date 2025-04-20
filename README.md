Uploading and Downloading Images from MySQL Databases in Python




/ Create a new user
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


// terminologies - collections, documents, schemas, keys, models


code                      database
mongoose.connect  -->    database create 
model create      -->    collection
CREATE CODE       -->    DOCUMENT
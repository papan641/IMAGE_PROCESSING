const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const listingSchema = new Schema({
    title:{ 
        type: String,
        required: true,
    },
    description: String,
    image: {
        type: String,
        set: (v) => v === ""? "https://www.vecteezy.com/photo/14001155-amazing-beach-landscape-super-wide-panoramic-exotic-travel-background-luxury-travel-idyllic-couple-honeymoon-love-destination-sunny-sea-sand-sky-exotic-resort-coast-palm-lagoon-seascape-banner" :v
    },
    price: Number,
    location: String,
    country: String,
});

const Listing = mongoose.model("Listing", listingSchema);
module.exports =Listing;



#code
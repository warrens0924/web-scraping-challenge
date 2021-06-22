from flask import Flask, render_template, redirect
import pymongo
from scrape_mars import scrape_info

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.scrape_data
mars_info = db.mars_info


@app.route("/")
def index():
    # Find one record of data from the mongo database
    mars_data = mars_info.find()

    # Return template and data
    return render_template("index.html", mars_data=mars_data)


@app.route("/scrape")
def scrape_info():

    mars_data = scrape_info()


    mars_info.insert_one(mars_data)

    listings = mongo.db.mars_page
    listings.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
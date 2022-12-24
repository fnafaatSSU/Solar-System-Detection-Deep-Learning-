import requests
from bs4 import BeautifulSoup

# Set the state for which you want to download satellite images
state = "massachusetts"

# Set the URL of the website that has the satellite images
url = "https://maps.massgis.digital.mass.gov/MassMapper/MassMapper.html?bl=MassGIS%20Basemap__100&l=massgis%3AGISDATA.COQ2021INDEX_POLY__GISDATA.COQ2021INDEX_POLY%3A%3ALabels__ON__100%2Cmassgis%3AGISDATA.COQ2021INDEX_POLY__GISDATA.COQ2021INDEX_POLY%3A%3ADefault__ON__48&b=-73.69628906250001%2C41.104190944576466%2C-69.74121093750001%2C43.014689161895184/{}".format(state)

# Initialize a counter for the number of images downloaded
counter = 0

while counter < 200:
    # Send a GET request to the website
    response = requests.get(url)

    # Parse the HTML content of the website
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the links to the satellite images on the website
    links = soup.find_all("a")

    # Iterate through the links and download the images
    for link in links:
        # Get the URL of the image
        image_url = link["href"]
        # Send a GET request to download the image
        image_response = requests.get(image_url)
        # Save the image to a file
        with open("satellite-image-{}.jpg".format(counter), "wb") as f:
            f.write(image_response.content)
        # Increment the counter
        counter += 1
        # Break the loop if we have downloaded enough images
        if counter >= 200:
            break

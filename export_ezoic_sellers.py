import csv
import json
import requests

# Get the URL from the user
url = input('Enter the URL: ')

# Fetch the JSON data from the URL
response = requests.get(url)

# Parse the JSON data
data = json.loads(response.text)

# Open a CSV file for writing
with open('sellers.csv', 'w', newline='') as csvfile:
  # Create a CSV writer
  writer = csv.writer(csvfile)

  # Write the headers
  writer.writerow(['seller_id', 'seller_type', 'name', 'domain'])

  # Loop through the data and write the rows
  for seller in data['sellers']:
    writer.writerow([seller['name'], seller['domain'], seller['seller_id'], 
seller['seller_type']])


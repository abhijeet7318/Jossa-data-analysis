import requests
import csv
from bs4 import BeautifulSoup

# Specify the URL of the page you want to scrape
url = 'https://josaa.admissions.nic.in/seatinfo/root/seatmatrixinfo.aspx'

# Send a GET request to the specified URL
response = requests.get(url).text

# Create a BeautifulSoup object with the response content and specify the parser
soup = BeautifulSoup(response, 'html.parser')

# Find the table element containing the data
table = soup.find_all('table', {'id': 'GridView1'})

# Extract the table headers
headers = []
header_row = table.find('tr')
for header in header_row.find_all('th'):
    headers.append(header.text.strip())

# Extract the table rows
rows = []
data_rows = table.find_all('tr')[1:]  # Skip the header row
for row in data_rows:
    row_data = []
    for cell in row.find_all('td'):
        row_data.append(cell.text.strip())
    rows.append(row_data)

# Define the path and filename for the CSV file
csv_file = 'data.csv'

# Write the data to the CSV file
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # Write the header row to the CSV file
    writer.writerow(headers)
    
    # Write the data rows to the CSV file
    for row in rows:
        writer.writerow(row)


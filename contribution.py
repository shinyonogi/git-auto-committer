import requests
from bs4 import BeautifulSoup

# Specify the GitHub username
username = 'shinyonogi'

# Make a GET request to the GitHub profile page
url = f'https://github.com/{username}'
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the contribution calendar SVG element
svg_element = soup.find('svg', class_='js-calendar-graph-svg')

# Extract the data from the SVG element
data = svg_element.find_all('rect')

# Process the contribution data
for rect in data:
    date = rect['data-date']
    count = rect['data-level']
    print(f"Date: {date}, Count: {count}")
    #Count: {count}


# Make a GET request to the GitHub API for user contributions
url = f'https://api.github.com/users/{username}/events'
response = requests.get(url)

# Process the response data
if response.status_code == 200:
    events = response.json()
    for event in events:
        if event['type'] == 'PushEvent':
            date = event['created_at'][:10]
            commit_count = len(event['payload']['commits'])
            print(f"Date: {date}, Commit Count: {commit_count}")
else:
    print("Failed to retrieve user contributions.")

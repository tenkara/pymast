# from datetime import datetime

# now = datetime.now()
# print("The time now is ", now)

# print("what date would you like to travel to?")
# user_date = input("Please enter a date in the format YYYY-MM-DD: ")

# print("You entered: ", user_date)

import requests
from bs4 import BeautifulSoup

# URL = f"https://www.billboard.com/charts/hot-100/{user_date}"
URL = "https://www.billboard.com/charts/hot-100/2012-12-31"
print(URL)

response = requests.get(URL)
# print (response)

website_html = response.text
# print(website_html)

soup = BeautifulSoup(website_html, "lxml")
# print(soup.title)

# all_songs = soup.find_all("h3","title-of-a-story")
all_songs = soup.find_all("h3","a-no-trucate")
# print(all_songs)

song_titles = [song.getText(strip=True) for song in all_songs]

print(song_titles)











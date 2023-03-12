import requests
from bs4 import BeautifulSoup

# Set the English language
headers = {"Accept-Language": "en-US, en;q=0.5"}
# Define URL for departures schedule
url = 'https://www.airport-athens.com/aia-departures'

# Send a GET request t othe URL
responese = requests.get(url, headers=headers)
html_content=responese.content

soup = BeautifulSoup(html_content, 'html.parser')


flight_shedule_dest = soup.findAll('div', {'class':'flight-row'})
#print(flight_shedule_dest[1].b.text)
Flight_Shedule_table=[]
for x in range(10,45):
  #Destination 
  destination=flight_shedule_dest[x].b.text
  #Destination_short
  destination_short=flight_shedule_dest[x].span.text
  #Time Departure + cleaning data
  time_departure=flight_shedule_dest[x].find('div', {'class':'flight-col flight-col__hour'})
  time_departure=time_departure.text
  time_departure=time_departure.strip()
  #Status + Cleaning data
  status_departure=flight_shedule_dest[1].find('div', {'class':'flight-col flight-col__status flight-col__status--G'})
  status_dep=status_departure.a.text
  status_dep=status_dep.replace(' [+]','')
  Flight_Shedule_table.append([destination,destination_short,time_departure,status_dep])
  #print(destination+":"+destination_short+":"+time_departure+':'+status_dep)

for line in Flight_Shedule_table:
  print(line[0]+"|"+line[1]+"|"+line[2]+"|"+line[3])



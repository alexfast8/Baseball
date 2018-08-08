from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.fangraphs.com/pitchfx.aspx?playerid=12808&position=P&pitch=all').text
soup = BeautifulSoup(source, 'lxml')

# csv_file = open('PD.csv','w') 

# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['pitch', 'thrown', 'O-Swing']) 
FB = soup.find(class_= 'rgAltRow', id= 'PFXOverview1_dgSeason4_ctl00__9')
FB_two = FB.find(class_= 'grid_line_regular')

print(FB.prettify())
print(FB_two.prettify())
# csv_writer.writerow([FB])
# csv_file.close()
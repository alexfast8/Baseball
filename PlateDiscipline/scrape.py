from bs4 import BeautifulSoup
import requests
import csv

#here is the URL I am scraping everything from
source = requests.get('https://www.fangraphs.com/pitchfx.aspx?playerid=12808&position=P&pitch=all').text
soup = BeautifulSoup(source, 'lxml')

#here is my csv as well as all of the different names of the columsns that I want
csv_file = open('PD.csv','w') 
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['year', 'pitch', 'abv','thrown', 'O-Swing', 'Z-Swing', 'Swing', 'O-Contact', 'Z-Contact', ' Contact', 'Zone', 'SwSt', 'pVAL', 'pVAL/C']) 

#here is where I scrape thru the HTML to find the information I need
FB = soup.find(class_= 'rgAltRow', id= 'PFXOverview1_dgSeason4_ctl00__9')

#this is virtually the same thing as above but gathered in a different way
FB_two = FB.find_all(class_= 'grid_line_regular')

#this is me converting everything to text
FB_Text = FB.text

print(FB_Text)
print(FB_two)

#the below was me trying a different way to get this properly. 
# print(FB.prettify())
# print(FB_two.prettify())

csv_writer.writerow([FB_Text])
csv_file.close()


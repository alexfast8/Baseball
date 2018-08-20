from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.fangraphs.com/pitchfx.aspx?playerid=12808&position=P&pitch=all').text
soup = BeautifulSoup(source, 'lxml')


csv_file = open('PD.csv','w') 

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['year', 'pitch', 'abv','thrown', 'O-Swing', 'Z-Swing', 'Swing', 'O-Contact', 'Z-Contact', ' Contact', 'Zone', 'SwSt', 'pVAL', 'pVAL/C']) 

FB = soup.find(class_= 'rgAltRow', id= 'PFXOverview1_dgSeason4_ctl00__9')
FB_two = FB.find_all(class_= 'grid_line_regular')

FB_Text = FB.text

print(FB_Text)
print(FB_two)
# print (FB.text)
# print (FB_two.text)

# print(FB.prettify())
# print(FB_two.prettify())

csv_writer.writerow([FB_Text])
csv_file.close()


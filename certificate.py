#Sourasish Certificate Generator
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

df = pd.read_excel('names.xlsx')

img = Image.open('certificate_template.png')

font = ImageFont.truetype('fontss.ttf', 120)
color = (0, 0, 0)  # black

for index, row in df.iterrows():
    name = row['Name']
    stream = row['Stream']
    
    cert = Image.new('RGB', img.size, (255, 255, 255))
    
    cert.paste(img, (0, 0))
    
    draw = ImageDraw.Draw(cert)
    name_x, name_y = 2000, 1145
    stream_x, stream_y = 1600, 1270
    draw.text((name_x, name_y), name, font=font, fill=color, anchor='mm')
    draw.text((stream_x, stream_y), stream, font=font, fill=color, anchor='mm')
    
    cert.save(f'{name}_certificate.png')

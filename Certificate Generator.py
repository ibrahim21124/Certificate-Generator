from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
df = pd.read_csv('Certificate List.csv')
font = ImageFont.truetype('arial.ttf',60)
for index,j in df.iterrows():
    img = Image.open('Certificate Template.jpg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(725,760),text='{}'.format(j['name']),fill=(0,0,0),font=font)
    img.save('Certificate/{}.jpg'.format(j['name']))
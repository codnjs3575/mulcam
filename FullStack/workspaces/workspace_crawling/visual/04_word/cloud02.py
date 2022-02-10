from wordcloud import WordCloud
import json
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

with open('webtoons.json',encoding='utf-8') as f :
    webtoons = json.load(f)

res = dict()
for webtoon in webtoons['webtoons']:
    res[webtoon['title']] = int(float(webtoon['star']) * 100)

masking_img = np.array(Image.open('kakao.png'))
cloud = WordCloud(font_path = 'Goyang.otf', max_font_size=40,
                  mask = masking_img, background_color='white').fit_words(res)
cloud.to_file('cloud02.png')

plt.imshow(cloud,interpolation='bilinear')
plt.axis('off')
plt.show()
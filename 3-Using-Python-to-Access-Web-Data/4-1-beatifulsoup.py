
import urllib.request as ur
from bs4 import *

url = "http://py4e-data.dr-chuck.net/comments_953223.html"

html = ur.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

count_of_spans = 0
sum = 0

spans = soup('span')
for span in spans:
    sum += int(span.contents[0])
    count_of_spans += 1

print('Count ', count_of_spans)
print('Sum ', sum)
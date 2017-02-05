import re

def open_html(f):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    return content
content = open_html(r'C:\Users\Никита\Desktop\hw14 (families)\arbuz.html')
Link = r'<a href="/wiki/(Amaryllidaceae|Amaranthaceae|Brassicaceae|Chenopodiaceae|Compositae|Cucurbitaceae|Gramineae|Leguminosae|Solanaceae|Umbelliferae)" class="mw-redirect" title="(Amaryllidaceae|Amaranthaceae|Brassicaceae|Chenopodiaceae|Compositae|Cucurbitaceae|Gramineae|Leguminosae|Solanaceae|Umbelliferae)">(.*?)</a>'
links = re.findall(Link, content)

for link in links[:10]:
    result = link[2]

tu = open('dz.txt', 'w').write((result))
file = open('dz.txt').read()
print('в файле должно оказаться:', file)

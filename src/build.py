"""Собирает index.html: подставляет картинки из src/img прямо в страницу (base64).

Запуск из корня репозитория:  python3 src/build.py
"""
import base64
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'src', 'index.src.html')
IMG = os.path.join(ROOT, 'src', 'img')
OUT = os.path.join(ROOT, 'index.html')


def inline(match):
    path = os.path.join(IMG, match.group(1) + '.jpg')
    with open(path, 'rb') as f:
        return 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode()


with open(SRC, encoding='utf-8') as f:
    html = re.sub(r'%%IMG_([a-z\-]+)%%', inline, f.read())
with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'index.html: {len(html) // 1024} KB')

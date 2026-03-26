import os
import re
import requests
from bs4 import BeautifulSoup

# Configuración
html_path = '/home/ubuntu/cafe-la-lucha/index.html'
img_dir = '/home/ubuntu/cafe-la-lucha/images'
os.makedirs(img_dir, exist_ok=True)

# Leer el HTML
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Buscar todas las etiquetas img y estilos con background-image
images = []

# De etiquetas img
for img in soup.find_all('img'):
    if img.get('src'):
        images.append(img['src'])

# De estilos inline o clases específicas (como hero-grain)
# Buscamos URLs en el contenido del HTML (regex para URLs de imágenes)
urls = re.findall(r'url\((.*?)\)', html_content)
for url in urls:
    # Limpiar comillas si existen
    clean_url = url.strip("'\"")
    images.append(clean_url)

# Descargar imágenes
image_map = {}
for i, url in enumerate(set(images)):
    try:
        print(f"Descargando: {url}")
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            # Determinar extensión (por defecto .jpg si no se puede determinar)
            ext = '.jpg'
            if 'image/png' in response.headers.get('Content-Type', ''):
                ext = '.png'
            elif 'image/webp' in response.headers.get('Content-Type', ''):
                ext = '.webp'
            
            filename = f"img_{i}{ext}"
            filepath = os.path.join(img_dir, filename)
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            image_map[url] = f"images/{filename}"
            print(f"Guardado como: {filename}")
    except Exception as e:
        print(f"Error descargando {url}: {e}")

# Actualizar el HTML con las nuevas rutas
new_html = html_content
for old_url, new_path in image_map.items():
    new_html = new_html.replace(old_url, new_path)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("\nHTML actualizado con éxito.")

import os
import requests

# Configuración
html_path = '/home/ubuntu/cafe-la-lucha/index.html'
img_dir = '/home/ubuntu/cafe-la-lucha/images'
os.makedirs(img_dir, exist_ok=True)

# Leer el HTML
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Lista de URLs encontradas manualmente para asegurar que no falte ninguna
urls = [
    "https://lh3.googleusercontent.com/aida/ADBb0ujkHuAP6euJLOLuCxPY6txvEL4P66sasMuAkRvxJnevXyE3N1UzDheSfYNiwutTwBqH5It57zUPr9uGutcYihp1Dm3ET2XTzwn0BS3-MBnnYRJLYqCNu6a0BK0UcHux403GDQuHjr2dvO_eXXhr8w9vJCo0gsI6-Ju_b1fDv_Dnk4_0Ax-UAMN4l-nK0uoOEDSP-RKbL2YNpSzMu092RDqR9dARlTgQRHercLi6oXJ8_CNN5H8XTH6eB28JM7y1809cjO2dnFc5Dg",
    "https://lh3.googleusercontent.com/aida/ADBb0uhs8qX3k3ySVThYfHzyOALFLN1vhNUz7Zeow-M8OGOxFvigaeRwPG2rkOJnmMp_Ky8nH7DUwH64Ir0i8-e2USdljr_PyIWHiU5yyNGmeMrSry_yyufIm5vPwlaQ_zJzhbUk08HFU4JBaVyOPPJ7VgauhNHAsuaIUytQFfcO5MeUTPUKctkma-HIm3FNYJ_F8txpLQ0QNIQJSzZeNoZIERuKh9Fy4CmKuy4tpvTVM93gdvkwTkfRYKDvHqC48UD0BNhWO8Ba2knj8w",
    "https://lh3.googleusercontent.com/aida/ADBb0ugODRIgtCmOPz8WydprvxcKVeA3UdCAy_XlhQtjMxezEudISyo1GGNz_DYjv0jvYONjX-YfFyc3NFiRsYTlJeMt3BU9a8ABrDIJRLcvJ0ut60QAoz8hwduKp-ja8AqD4zfJhE9nWJOtgvQVZ7ktpV3-pPWf1jROm5UxB2RRtn3a1jZH2K9fieomxoykQcphCUvrXopfCZWsX-yubTi-6bNWykB5LCXwwPcgkU5ysjLL5kAhlt5jIFrIztCEpbKirvZpHv2tU3OR3A",
    "https://lh3.googleusercontent.com/aida/ADBb0ujMExcBkPuDdHD8mLoquHXOi7jBFaxuJR1z0VRkLn-dEJ3qSf8q8ycCYKXUuyfUqJiqrWVUSlfSJOAhPuwJOFYsbdBjIwjo4Gk5IbS3SD_V2C4Pk9Qs9M-woafXelTlNwG4nx8cQ-MshEmhvOhBkFBEi5mf7wrqLgWvMbAX58TNWvwavMCm0bH8qMX0LMr2DdKNJAcDZaTCg1899E9w0aqeObsS9AG_1vezKMzomrvgZYdcZGIzS_Jlud8XV9trEDp6jhS_FHnm8w",
    "https://lh3.googleusercontent.com/aida/ADBb0ugfiTun15k2b0Y4KhxPlpd-98pw5lFt3YmncO-ZsIPliDhlmqsd4eHgfGYqA0XmiE57fSIlUuSPtb95ZehCig3UW53HseMhtFS1Bfq1_bTaXpeShxxMBZuMA-KmOGteXqRfWNZdWbryf2B5idL81qGmtPc1FqHzj2fzMz_dY7Wzc_LST3wF-_9cyPZpu8ejb0QCg_HdSMDTW_uQYJ7j3yrE78a5wWOMVYF08ovze4aAHfWbFilAcukLbjwxRv0P9sIPd-PRKxZYpw",
    "https://lh3.googleusercontent.com/aida/ADBb0ui1YRQcuxLeMDz5x5ui43DjGCtKUbyxjdyRlHplb23Zx5wJcNn0gDgvcda1mFe4n7o0Dp0TIQYkIeyjZzFsYOf80tlWJi37EtY8dcpSBNLv6quQ35vGEwJLE2yFZ1a0RvzrSs-ZaHYrJZgBgmwRzBp0OX3yNVpW_xaww7miC4f__GvMh5GgUsq2IahNPC2Mvk6db72c-_fuzi4zu-qTzBsPA00wPFI6v1Z45CvH_Cj7IbNVXJ4SfflA3K7UfnO1AG7ltMIUdGK8pQ",
    "https://lh3.googleusercontent.com/aida/ADBb0ui4K2kHWePYM3gCbkzy49rrwI_A4_1fe0dC3r3CMEXgBy_tF29SXwDQlfI2ALLxmtNGnrEmOw2CXxiWkdWCmi3iXi3h4LMeKzW8i5LZCpO3PGzCPI13GN9MlXYTSrZhjGyiuCFsxSev9-sMkqVzGVd34JhrmBfvnVg8ul4mOvQ-qxlFneYMB8XuhZD-MSVilDg8pC6-xFmSQghJ7Hu7TBLufUacltYBoapzQXa1skBnmnINSj4OSdiCl-LdoVC1swQe8qe_oSTyug",
    "https://lh3.googleusercontent.com/aida/ADBb0ujiYouUqrAAqFO6NXstRGkVhEdmSvBPIQcZOfwsRRmb3vQP8UNMWy7u6VfIJ_dtTw6DfIbdMwjqGn5eFwUdfnCbaB4kxDs77Gm5_8kIEsapxT5eJRqQ-knAvMO3CbGoIzKUoL2vg39eGr7t-LZxPyVXb6wdlBhg5yJ_7-7fmFlkZrCwXkX8XlycZKIEZ3wiOFjf11x0E-BCzdoFQyk3SymbC0eamotjTxz1912m2ojb_39SlR4LJs-m4BtqjCFZdeEWQAVx8oh1bQ"
]

image_map = {}
for i, url in enumerate(urls):
    try:
        print(f"Descargando: {url}")
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            ext = '.jpg'
            content_type = response.headers.get('Content-Type', '')
            if 'image/png' in content_type: ext = '.png'
            elif 'image/webp' in content_type: ext = '.webp'
            
            filename = f"img_{i}{ext}"
            filepath = os.path.join(img_dir, filename)
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            image_map[url] = f"images/{filename}"
            print(f"Guardado como: {filename}")
    except Exception as e:
        print(f"Error descargando {url}: {e}")

# Actualizar el HTML
new_html = html_content
for old_url, new_path in image_map.items():
    new_html = new_html.replace(old_url, new_path)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print("\nHTML actualizado con éxito.")

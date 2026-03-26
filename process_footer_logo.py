from PIL import Image, ImageOps
import os

def process_logo(input_path, output_path):
    try:
        # Abrir la imagen original
        img = Image.open(input_path).convert("RGBA")
        
        # Separar los canales
        r, g, b, a = img.split()
        
        # Crear una versión blanca de la imagen
        # Invertimos los colores si es necesario o simplemente creamos una capa blanca con el mismo alfa
        white_img = Image.new("RGBA", img.size, (255, 255, 255, 255))
        
        # Usar el canal alfa original para la nueva imagen blanca
        final_img = Image.composite(white_img, Image.new("RGBA", img.size, (0, 0, 0, 0)), a)
        
        # Guardar la imagen procesada
        final_img.save(output_path)
        print(f"Logo procesado y guardado en: {output_path}")
        return True
    except Exception as e:
        print(f"Error procesando el logo: {e}")
        return False

if __name__ == "__main__":
    input_logo = "/home/ubuntu/cafe-la-lucha/new_images/img-003.jpg"
    output_logo = "/home/ubuntu/cafe-la-lucha/new_images/footer_logo_white.png"
    process_logo(input_logo, output_logo)

import base64
import os

def encode_images_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            image_path = os.path.join(directory, filename)
            base_name = os.path.splitext(filename)[0]  # Obtener el nombre base sin la extensión
            encoded_string = encode_image_to_base64(image_path)
            save_base64_to_file(encoded_string, base_name)

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_bytes = base64.b64encode(image_file.read())
        encoded_string = encoded_bytes.decode("utf-8")
    return encoded_string

def save_base64_to_file(encoded_string, base_name):
    base64_dir = "./base64"
    os.makedirs(base64_dir, exist_ok=True)  # Crear el directorio "./base64" si no existe
    txt_path = os.path.join(base64_dir, base_name + ".txt")
    with open(txt_path, "w") as txt_file:
        txt_file.write(encoded_string)
    print("Imagen codificada en base64 guardada en:", txt_path)

# Directorio que contiene las imágenes
directory = "./images"

# Codificar en base64 todas las imágenes en el directorio
encode_images_in_directory(directory)

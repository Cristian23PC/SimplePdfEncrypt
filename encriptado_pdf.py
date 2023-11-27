#!/bin/python3
#Librerias
from pypdf import PdfReader, PdfWriter
import time
import sys

archivo_pdf = input("Ingrese el nombre del archivo pdf que desea encripitar (con extension): ")
reader = PdfReader(archivo_pdf)
writer = PdfWriter()

# Add all pages to the writer
for page in reader.pages:
    writer.add_page(page)

# Add a password to the new PDF
contrasena = input("Ingrese la contraseña para encriptar el archivo: ")
writer.encrypt(contrasena, algorithm="AES-256")
#Moneria
def loading_animation():
    animation = "Encriptando.... "
    for _ in range(20):  # Número de iteraciones para simular el movimiento
        sys.stdout.write('\r' + animation)
        sys.stdout.flush()
        time.sleep(0.1)  # Ajusta el tiempo de espera según sea necesario
        animation = animation[1:] + animation[0]

    print("\nDone!")

# Llamar a la función para iniciar la animación
loading_animation()
# Save the new PDF to a file
archivo_salida = input("Ingrese el nombre para guardar el archivo (sin extension): ")
with open(archivo_salida + "_protegido.pdf", "wb") as f:
    writer.write(f)
print("Archivo encriptado correctamente y guardado en carpeta local".center(20,'-'))

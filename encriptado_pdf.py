import sys
import os
from PyPDF2 import PdfReader, PdfWriter
import time

def cargar_pdf(ruta_pdf):
    with open(ruta_pdf, 'rb') as file:
        reader = PdfReader(file)
        writer = PdfWriter()

        # Agregar todas las páginas al escritor
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            writer.add_page(page)

        # Agregar una contraseña al nuevo PDF
        contrasena = input("Ingrese la contraseña para encriptar el archivo: ")
        writer.encrypt(contrasena)

        # Monitoreo
        print("-" * 50)
        def loading_animation():
            animation = "Encriptando.... "
            for _ in range(20):
                sys.stdout.write('\r' + animation)
                sys.stdout.flush()
                time.sleep(0.1)
                animation = animation[1:] + animation[0]

            print("\n¡Listo!")

        loading_animation()
        print("-" * 50)

        # Obtener el directorio y el nombre del archivo original
        directorio_original, nombre_base = os.path.split(ruta_pdf)

        # Construir la ruta completa del nuevo archivo PDF
        nombre_sin_extension = os.path.splitext(nombre_base)[0]
        ruta_salida = os.path.join(directorio_original, nombre_sin_extension + "_protegido.pdf")

        with open(ruta_salida, "wb") as f:
            writer.write(f)

        print(f"Archivo encriptado correctamente y guardado como {nombre_sin_extension}_protegido.pdf en la misma carpeta que el archivo original".center(50, '-'))

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != "-archivo":
        print("Uso: python pdf_encriptador.py -archivo <ruta_del_archivo>")
    else:
        ruta_archivo = sys.argv[2]
        if not os.path.isfile(ruta_archivo):
            print("¡La ruta proporcionada no es un archivo válido!")
        else:
            cargar_pdf(ruta_archivo)

import requests
import os

# Verificar y mostrar la ruta completa de los archivos
print("Ruta completa de 'generator_code_vf.py':", os.path.abspath("generator_code_vf.py"))
print("Ruta completa de 'uploader_code_vf.py':", os.path.abspath("uploader_code_vf.py"))
print("Ruta completa de 'Informe_Economico_473214_vf.docx':", os.path.abspath("Informe_Economico_473214_vf.docx"))

token = "473214"
url = f"https://c40training.com/C40trainingAPI/api/upload/code?token={token}"

print("Abriendo los archivos para subir...")
try:
    files = {
        'file': open("generator_code_vf.py", "rb"),  # Archivo Python con el generador
        'file': open("uploader_code_vf.py", "rb"),   # Archivo Python para subir
        'file': open("Informe_Economico_473214_vf.docx", "rb"),  # Documento Word generado
    }

    print("Archivos abiertos exitosamente.")

    print("Enviando solicitud POST para subir los archivos...")
    response = requests.post(url, files=files)
    print("Solicitud enviada. Procesando respuesta...")

    print(f"Estado de la respuesta: {response.status_code}")
    print("Contenido de la respuesta:")
    response_data = response.json()
    print(response_data)

    # Verificar si todos los archivos esperados están en la respuesta
    expected_files = ["generator_code_vf.py", "uploader_code_vf.py", "Informe_Economico_473214_vf.docx"]
    uploaded_files = response_data.get('message', '').split(':')[-1].strip().split(', ')

    for file in expected_files:
        if file in uploaded_files:
            print(f"El archivo '{file}' se ha subido correctamente.")
        else:
            print(f"El archivo '{file}' no se encuentra en la carpeta.")

finally:
    # Asegurarse de cerrar los archivos
    for file in files.values():
        file.close()

# Añadir impresión para verificar que los archivos están siendo preparados para la solicitud
print("Preparando archivos para la solicitud POST...")
for filename, file in files.items():
    print(f"Archivo '{filename}' preparado para enviar: {file.name}")


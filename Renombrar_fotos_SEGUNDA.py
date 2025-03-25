import os

# Carpeta donde están las fotos
carpeta = "C5_VIERNES"

# Prefijo para el nuevo nombre
prefijo = "clase5_foto"

# Enumerar los archivos en la carpeta
for i, nombre_archivo in enumerate(os.listdir(carpeta), start=1):
    # Filtrar archivos que sean imágenes (por ejemplo, .jpg, .png, etc.)
    # O simplemente procesa todos los archivos
    if nombre_archivo.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        # Extraer la extensión original
        _, extension = os.path.splitext(nombre_archivo)
        
        # Construir el nuevo nombre de archivo
        nuevo_nombre = f"{prefijo}{i}{extension}"
        
        # Rutas completas (antes y después)
        ruta_vieja = os.path.join(carpeta, nombre_archivo)
        ruta_nueva = os.path.join(carpeta, nuevo_nombre)
        
        # Renombrar
        os.rename(ruta_vieja, ruta_nueva)
        print(f"Renombrado: {nombre_archivo} -> {nuevo_nombre}")

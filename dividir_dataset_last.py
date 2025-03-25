##Dividir las imágenes para entrenamiento, validación y testeo##

import os
import shutil
from sklearn.model_selection import train_test_split

# Rutas de las carpetas de cada categoría
carpeta_categoria1 = "recortadas_C2"
carpeta_categoria2 = "recortadas_C3"
carpeta_categoria3 = "recortadas_C5"

# Crear carpetas para entrenamiento, validación y test
os.makedirs("entrenamiento/categoria1", exist_ok=True)
os.makedirs("entrenamiento/categoria2", exist_ok=True)
os.makedirs("entrenamiento/categoria3", exist_ok=True)

os.makedirs("validacion/categoria1", exist_ok=True)
os.makedirs("validacion/categoria2", exist_ok=True)
os.makedirs("validacion/categoria3", exist_ok=True)

os.makedirs("test/categoria1", exist_ok=True)
os.makedirs("test/categoria2", exist_ok=True)
os.makedirs("test/categoria3", exist_ok=True)

# Función para dividir y mover imágenes
def dividir_imagenes(carpeta_origen, carpeta_entrenamiento, carpeta_validacion, carpeta_test, test_size=0.10, val_size=0.1111):
    # Listar todas las imágenes
    imagenes = os.listdir(carpeta_origen)
    
    # Dividir en entrenamiento+validación y test
    train_val, test = train_test_split(imagenes, test_size=test_size, random_state=42)
    
    # Dividir entrenamiento+validación en entrenamiento y validación
    train, val = train_test_split(train_val, test_size=val_size, random_state=42)
    
    # Mover imágenes a las carpetas correspondientes
    for img in train:
        shutil.copy(os.path.join(carpeta_origen, img), os.path.join(carpeta_entrenamiento, img))
    for img in val:
        shutil.copy(os.path.join(carpeta_origen, img), os.path.join(carpeta_validacion, img))
    for img in test:
        shutil.copy(os.path.join(carpeta_origen, img), os.path.join(carpeta_test, img))

# Dividir imágenes para cada categoría
dividir_imagenes(carpeta_categoria1, "entrenamiento/categoria1", "validacion/categoria1", "test/categoria1")
dividir_imagenes(carpeta_categoria2, "entrenamiento/categoria2", "validacion/categoria2", "test/categoria2")
dividir_imagenes(carpeta_categoria3, "entrenamiento/categoria3", "validacion/categoria3", "test/categoria3")

print("División del dataset completada.")


##Aumentación de datos##
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from PIL import Image
import numpy as np
import os

# Función para aplicar data augmentation
def aplicar_data_augmentation(carpeta_origen, carpeta_destino, num_imagenes_a_generar):
    # Configurar el generador de data augmentation
    datagen = ImageDataGenerator(
        rotation_range=30,       # Rotación aleatoria entre -30° y 30°
        width_shift_range=0.1,   # Desplazamiento horizontal aleatorio (10% del ancho)
        height_shift_range=0.1,  # Desplazamiento vertical aleatorio (10% del alto)
        shear_range=0.2,         # Inclinación aleatoria
        zoom_range=0.2,          # Zoom aleatorio (80% a 120%)
        horizontal_flip=True,    # Volteo horizontal aleatorio
        vertical_flip=True,      # Volteo vertical aleatorio
        brightness_range=[0.8, 1.2],  # Rango de ajuste de brillo
        #fill_mode='nearest'      # Rellenar pixeles vacíos con el valor más cercano
    )
    
    # Listar todas las imágenes en la carpeta de origen
    imagenes = os.listdir(carpeta_origen)
    
    # Calcular cuántas imágenes artificiales generar por imagen real
    num_imagenes_reales = len(imagenes)
    num_imagenes_por_real = num_imagenes_a_generar // num_imagenes_reales
    resto = num_imagenes_a_generar % num_imagenes_reales
    
    # Procesar cada imagen
    for i, img_name in enumerate(imagenes):
        # Ruta completa de la imagen
        img_path = os.path.join(carpeta_origen, img_name)
        
        # Cargar la imagen
        img = Image.open(img_path)
        img_array = np.array(img)  # Convertir a array de NumPy
        img_array = np.expand_dims(img_array, axis=0)  # Añadir dimensión de lote
        
        # Calcular cuántas imágenes generar para esta imagen real
        if i < resto:
            num_a_generar = num_imagenes_por_real + 1
        else:
            num_a_generar = num_imagenes_por_real
        
        # Generar imágenes aumentadas
        j = 0
        for batch in datagen.flow(img_array, batch_size=1, save_to_dir=carpeta_destino, save_prefix=f'aug_{os.path.splitext(img_name)[0]}', save_format='jpg'):
            j += 1
            if j >= num_a_generar:
                break  # Detener después de generar el número deseado de imágenes

# Número objetivo de imágenes por categoría en el entrenamiento
num_imagenes_objetivo = 2000  # Puedes ajustar este número según tus necesidades

# Aplicar data augmentation a cada categoría en el entrenamiento
aplicar_data_augmentation("categoria_2", "categoria_2", num_imagenes_objetivo - len(os.listdir("categoria_2")))
aplicar_data_augmentation("categoria_3", "categoria_3", num_imagenes_objetivo - len(os.listdir("categoria_3")))
aplicar_data_augmentation("categoria_5", "categoria_5", num_imagenes_objetivo - len(os.listdir("categoria_5")))

print("Data augmentation aplicado para balancear las clases.")


import os
import shutil
import threading
import time

def delete_static_contents():
    static_path = 'static'

    # Verificar si el directorio existe
    if os.path.exists(static_path):
        # Eliminar todos los archivos en el directorio
        for filename in os.listdir(static_path):
            file_path = os.path.join(static_path, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Error al eliminar {file_path}: {e}')
    else:
        print('El directorio static no existe.')

def delete_static_contents_periodically():
    while True:
        # Llamar a la función para eliminar el contenido
        delete_static_contents()

        # Dormir durante 2 horas antes de volver a ejecutar la función
        time.sleep(2 * 60 * 60)  # 2 horas en segundos

# Crear un hilo para ejecutar la función periódicamente
delete_thread = threading.Thread(target=delete_static_contents_periodically)

# Iniciar el hilo
delete_thread.start()
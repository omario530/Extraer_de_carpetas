import os
import shutil

# Ruta de la carpeta
ruta = r"C:\Users\omar.escamilla\Documents\Renombrar_Escaneados_v2\escaneados"

# Carpetas
archivos = os.listdir(ruta)

# seleccionar cada carpeta
i = 0
ii = 1
while i < len(archivos):
    if os.path.isfile(ruta + "/" + archivos[i]) == False:
        print(archivos[i])
        archivos_2 = os.listdir(ruta + "/" + archivos[i])

        for ii in range(len(archivos_2)):
            print(archivos_2[ii])
            shutil.copy2(ruta + "/" + archivos[i] + "/" + archivos_2[ii], ruta + "/" + archivos_2[ii])
            ii += 1
    i += 1



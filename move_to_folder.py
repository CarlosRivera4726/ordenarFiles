import os

def buscarGeneral(tipoArchivo):
    i=0
    archivos = os.listdir()
    archivosGenerales = []
    while i < len(archivos):
        if archivos[i].find(tipoArchivo) != -1 :
            archivosGenerales.append(archivos[i])
            i += 1
        else:
            i += 1
    return archivosGenerales
def moverADirectorio(archivos,carpetaDestino):
    try:
        if len(archivos) != 0:
            for i in archivos:
                os.system("move "+ '"'+i+'"'+" "+carpetaDestino)
    except:
        print("Error al mover el archivo")

def crearDirectorio(nombreDirectorio):
    return os.system("mkdir "+nombreDirectorio)

archivosRar = buscarGeneral(".rar")
archivosZip = buscarGeneral(".zip")
archivosPdf = buscarGeneral(".pdf")
archivosExe = buscarGeneral(".exe")
archivosDocx = buscarGeneral(".docx")
archivosjpg = buscarGeneral(".jpg")
archivoslnk = buscarGeneral(".lnk")
archivosPng = buscarGeneral(".png")
archivosJpeg = buscarGeneral(".jpeg")
archivosTxt = buscarGeneral(".txt")

try:
    crearDirectorio("RAR's")
    crearDirectorio("ZIP's")
    crearDirectorio("EXE's")
    crearDirectorio("DOCX's")
    crearDirectorio("IMG")
    crearDirectorio("ACCESOSDIRECTOS")
    crearDirectorio("TEXTOS")
except:
    print("YA EXISTEN LOS DIRECTORIOS\n")
directorioDocx = "DOCX's"
try:
    print("MOVIENDO ARCHIVOS\n\n")

    moverADirectorio(archivosRar,"RAR's")
    moverADirectorio(archivosPdf, "PDF's")
    moverADirectorio(archivosDocx, "DOCX's")
    moverADirectorio(archivosjpg, "IMG")
    moverADirectorio(archivoslnk, "ACCESOSDIRECTOS")
    moverADirectorio(archivosPng, "IMG")
    moverADirectorio(archivosJpeg, "IMG")
    moverADirectorio(archivosTxt, "TEXTOS")
except:
    print("NO FUE POSIBLE MOVER EL/LOS ARCHIVOS!")

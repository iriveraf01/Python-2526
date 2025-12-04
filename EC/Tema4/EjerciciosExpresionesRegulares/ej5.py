# Ejercicio 5
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con
# extension .txt
texto = "file1.txt file2.pdf image.png document.docx notes.txt secreto.txt"
import re
coincidencias = re.findall(r"\w+\.txt", texto)
print(coincidencias)
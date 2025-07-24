# entropy-script
Script de Python para calcular la entropía de Shannon de archivos binarios, útil para el análisis de malware desempaquetado (unpacked) o evaluación de aleatoriedad en datos. Ideal para principiantes en ciberseguridad. Incluye instrucciones básicas y puede ejecutarse en Linux.

## Requisitos
- Python 3.x
- Sistema operativo Linux (probado en Ubuntu)
- Acceso a un archivo binario para analizar

## Instrucciones

- Clone el repositorio en su equipo.
- Reemplace el apartado de 'your_file' por la ruta del archivo al que le desea calcular su entropía.
- Obtendrá el resultado con hasta 6 decimales, por ejemplo: Entropía: 6.550600.

## Precauciones

- Usa este script solo en un entorno seguro, como una máquina virtual (ej. VirtualBox con Ubuntu), especialmente si analizas malware.
- No ejecutes los archivos maliciosos en tu sistema principal.
- Asegúrate de tener permisos adecuados para leer los archivos.
- Asegúrate que el archivo está 'unpacked'. De lo contrario, puede no funcionar precisamente.


# Ciudades utilizadas:

Wollongong
Ballarat
MountGinini
Hobart
Williamtown
Adelaide
Sale
Penrith
Woomera
SalmonGums

# DOCKER

1. Ubicar la terminal en la carpeta "docker": Ejemplo en Windows 'cd C:\Users\Usuario\repos\AA1-TUIA-Bravi-Nemeth\docker'
2. Crear imagen: docker build -t infer-image .
3. Subir el archivo .csv a predecir en la carpeta "docker" con el nombre "weather_docker.csv"
4. Correr el contenedor: docker run --rm -v $(pwd):/output infer-image (linux) o docker run --rm -v ${PWD}:/output infer-image (windows)

   
En la misma carpeta se va a generar el archivo predicciones.csv

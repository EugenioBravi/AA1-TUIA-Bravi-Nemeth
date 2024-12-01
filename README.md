# Docker Setup

## Ciudades utilizadas

- Wollongong
- Ballarat
- Mount Ginini
- Hobart
- Williamtown
- Adelaide
- Sale
- Penrith
- Woomera
- Salmon Gums

## Pasos para usar Docker

1. **Ubicar la terminal en la carpeta "docker":**

   En Windows:

   ```bash
   cd \AA1-TUIA-Bravi-Nemeth\docker
   ```

2. **Crear la imagen Docker:**
   Ejecuta el siguiente comando para crear la imagen `infer-image`:

   ```bash
   docker build -t infer-image .
   ```

3. **Subir el archivo `.csv` a predecir:**

   Coloca el archivo `weather_docker.csv` en la carpeta `docker`.

4. **Correr el contenedor:**

   ```bash
   docker run --rm -v <ruta-especifica-de-la-carpeta-docker>:/app infer-image
   ```

   Esto generará el archivo `predicciones.csv` en la misma carpeta.

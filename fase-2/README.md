# Fase 2:

En esta fase del proyecto se configura una imagen de Docker usando Dockerfile. Esta imagen contendrá las librerias necesarias para que funcione los scripts train.py y predict.py los cuales se quemaran en la imagen también.
El contenedor tiene dos scripts:

predict.py: que dado un conjunto de datos de entrada como un fichero csv, emita una predicción para cada dato de entrada, usando un modelo previamente almacenado en disco.

train.py: que dado un conjunto de entrenamiento (datos más etiquetas), entrene de nuevo el modelo y guarde una versión nueva del mismo.

## Construir la imagen en docker:
**Ejecutar el comando:**

docker build -t ml-scripts .

# En Windows desde cmd:
## Ejecutar train.py:

docker run -v %CD%/output:/usr/src/app/output ml-scripts python train.py --data_file /usr/src/app/output/train_data.csv --model_file /usr/src/app/output/model.pkl --overwrite_model

El contenedor está montando el volumen output en el directorio /usr/src/app/output, lo que asegura que cualquier archivo creado o modificado en esa ruta persista en tu sistema anfitrión.

## Ejecutar predict.py:

docker run -v $%CD%/output:/usr/src/app/output ml-scripts python predict.py --input_file /usr/src/app/output/test_data.csv --model_file /usr/src/app/output/model.pkl --predictions_file /usr/src/app/output/predictions.csv

los resultados se almacenarán en ./output en el sistema local.

# En Linux desde bash:
## Ejecutar train.py:

docker run -v ${PWD}/output:/usr/src/app/output ml-scripts python train.py --data_file /usr/src/app/output/train_data.csv --model_file /usr/src/app/output/model.pkl --overwrite_model

El contenedor está montando el volumen output en el directorio /usr/src/app/output, lo que asegura que cualquier archivo creado o modificado en esa ruta persista en tu sistema anfitrión.

## Ejecutar predict.py:

docker run -v ${PWD}/output:/usr/src/app/output ml-scripts python predict.py --input_file /usr/src/app/output/test_data.csv --model_file /usr/src/app/output/model.pkl --predictions_file /usr/src/app/output/predictions.csv

los resultados se almacenarán en ./output en el sistema local.

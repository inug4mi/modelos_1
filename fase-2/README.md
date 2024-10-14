## Construir la imagen en docker:
**Ejecutar el comando:**

docker build -t ml-scripts .

## Ejecutar train.py como volumen en docker:

docker run -v $PWD/output:/usr/src/app/output ml-scripts python train.py --data_file /usr/src/app/output/train_data.csv --model_file /usr/src/app/output/model.pkl --overwrite_model

El contenedor está montando el volumen output en el directorio /usr/src/app/output, lo que asegura que cualquier archivo creado o modificado en esa ruta persista en tu sistema anfitrión.

## Ejecutar predict.py como volumen de docker:

docker run -v $PWD/output:/usr/src/app/output ml-scripts python predict.py --input_file /usr/src/app/output/test_data.csv --model_file /usr/src/app/output/model.pkl --predictions_file /usr/src/app/output/predictions.csv

Cada vez que ejecutes los scripts train.py o predict.py, los resultados se almacenarán en ./output en tu sistema local.

<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **Proyecto MLOps - Sistema de Recomendación de Videojuegos para Steam** </h1>

Este es el README para el proyecto individual número 1 de MLOps, en el cual se ha desarrollado un sistema de recomendación de videojuegos para la plataforma Steam.

## Descripción del Proyecto

El objetivo de este proyecto es crear un sistema de recomendación de videojuegos para los usuarios de Steam. Se abordaron múltiples aspectos del ciclo de vida de un proyecto de Machine Learning, desde la limpieza y transformación de datos hasta el despliegue de una API y la implementación de un modelo de recomendación. A continuación, se describen los principales componentes del proyecto:

### Data Engineering

Se realizó la limpieza y transformación de los datos disponibles, abordando problemas como datos anidados y datos en bruto (nulos, problemas de formato, entre otros). Esto incluyó la creación de un conjunto de datos preparado para su uso en la creación del sistema de recomendación. Nos vamos en librerias como gzip, json y pandas.

### Feature Engineering

Se creó una nueva columna llamada "sentiment_analysis" mediante análisis de sentimiento de las reseñas de usuarios basado en la libreria NLTK. Esto facilitará el trabajo de los modelos de Machine Learning y el análisis de datos. Adicional se trabajo con la libreria langdetect ya que los reviews venian con diferentes idiomas.

### API Desarrollada con FastAPI

Se desarrolló una API utilizando el framework FastAPI para poner a disposición de la empresa los datos procesados y las funcionalidades de consulta. La API incluye varios endpoints que permiten obtener información relevante sobre los videojuegos y usuarios. Que son los siguientes:

- TimeGenrePlay: Devuelve el año de lanzamiento con más horas reproducidas para el género ingresado.
- UserbyGenre: Devuelve el usuario que acumula más horas reproducidas para el género determinado y una lista de la acumulación de horas reproducidas por año.
- RecommendUsers: Devuelve los 3 juegos más recomendados por los usuarios para el año determinado (reviews.recommend = reseñas verdaderas y positivas/neutrales).
- NotRecommendUsers: Returns the top 3 recommended games by users for the given year (reviews.recommend = True and positive/neutral reviews).
- analysis_of_sentiment: Enter year to consult, to return the Number of reviews categorized by sentiment
- ecomendation_of_user: Ingrese el ID de usuario para devolver los juegos recomendados

### Despliegue en la Nube

La API se desplegó en la nube utilizando Render. Esto permite que la API sea accesible desde cualquier dispositivo conectado a Internet. Tener en cuenta que por ser la version gratuita de Render se tenia muy baja capacidad de memoria, lo que imposibilitaba cargarle grandes bases de datos o procesamiento logico de las misma, por ello se opto por generar todo el procesamiento logico de forma local, generando asi una base de datos que conteniera ya todas las respuestas a las consultas. De esta manera en render se generaba un minimo de consumo de memoria. Esta fue la unica forma que logramos dejarlo accesible desded cualquier dispositivo conectado a internet.


### Análisis Exploratorio de Datos (EDA)

Se llevó a cabo un análisis exploratorio de datos para investigar las relaciones entre las variables. El EDA se realizó manualmente para comprender mejor los datos disponibles, como lo fue la clasificacion de 0 ,1 o 2 del analisis de sentimientos y los idiomas en los en los que estaban escritos los reviews.

### Modelo de Recomendación

Se implementó un modelo de recomendación basado en filtro de usuario-ítem, lo que permite recomendar videojuegos relevantes a cada uno de los usuarios. Para este proceso se utilizo la libreria cosine_similarity de sklearn.

### Video de Presentación

Se creó un video de presentación que muestra el funcionamiento de la API y Render, y brinda una breve explicación del modelo de recomendación utilizado:
- https://www.youtube.com/watch?v=wVFX7P4oRVc

### Link del repositorio (GitHub)

Sitio donde esta todo alojado:
- https://github.com/Otaloravega/Fisrt_Project-MLops-Juan_Otalora

## Cómo Usar la API

La API se puede acceder a través de los siguientes endpoints:

- Link general del deployment: https://first-project-mlops-juan-otalora.onrender.com/

- TimeGenrePlay(genre: str): https://first-project-mlops-juan-otalora.onrender.com/TimeGenrePlay/{genre}

- UserbyGenre(genre: str): https://first-project-mlops-juan-otalora.onrender.com/UserbyGenre/{genre}

- RecommendUsers(year: int): https://first-project-mlops-juan-otalora.onrender.com/RecommendUsers/{year}

- NotRecommendUsers(year: int): https://first-project-mlops-juan-otalora.onrender.com/NotRecommendUsers/{year}

- analysis_of_sentiment(year: int): https://first-project-mlops-juan-otalora.onrender.com/analysis_of_sentiment/{year}

- recomendation_of_user(id: str): https://first-project-mlops-juan-otalora.onrender.com/recomendation_of_user/{id}

## Estructura del Repositorio

El repositorio está organizado de la siguiente manera:

- `Sources/`: Contiene los datos originales.
- `root/datos/`: Contiene los datos transformados para lectura de API.
- `root/main.py/`Contiene el código fuente de la API.
- `project_MLops_Juan_Otalora.ipynb/`Contiene el modelo de recomendación y todo el procesamiento end to end.
- `videos/`: Contiene el video de presentación.

## Requisitos de Instalación

Para ejecutar la API localmente, debes instalar las siguientes bibliotecas y dependencias:

```bash
pip install fastapi
pip install uvicorn
```

Si se quiere ejecutar el proyecto donde se desarrolla todo end to end ('Project_MLops_Juan_Otalora.ipynb') se debe tener instaladas las sigueintes librerias:

- gzip
- json
- matplotlib
- seaborn
- pandas
- numpy
- ast
- nltk
- langdetect
- sklearn
- tqdm
# Mapa Mental de Modelos de Machine Learning

Este proyecto es una aplicación web desarrollada con Flask que permite visualizar y gestionar información sobre diferentes modelos de Machine Learning.

## Características

*   **Visualización de Modelos:** Muestra una lista de modelos de Machine Learning con sus descripciones, fuentes e imágenes.
*   **Almacenamiento de Modelos:** Permite agregar y almacenar información sobre nuevos modelos en una base de datos SQLite.
*   **Interfaz Intuitiva:** Ofrece una interfaz web fácil de usar para explorar y administrar los modelos.

## Requisitos

*   Python 3.6+
*   Flask
*   Werkzeug
*   SQLite

## Instalación

1.  **Clona el repositorio:**

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_PROYECTO>
    ```

2.  **Crea un entorno virtual (recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    venv\Scripts\activate  # En Windows
    ```

3.  **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuración

1.  **Base de datos:**

    *   La aplicación utiliza una base de datos SQLite llamada `modelos.db`. Este archivo se creará automáticamente la primera vez que ejecutes la aplicación y accedas a la ruta `/almacenamiento`.

2.  **Clave secreta:**

    *   Asegúrate de establecer una clave secreta para tu aplicación Flask en el archivo `app.py`.  En un entorno de producción, ¡cámbiala por una clave segura y aleatoria!

    ```python
    app = Flask(__name__)
    app.secret_key = 'clave_secreta'  # ¡Cambia esto en producción!
    ```

## Ejecución

1.  **Ejecuta la aplicación:**

    ```bash
    python app.py
    ```

2.  **Accede a la aplicación:**

    *   Abre tu navegador y ve a la URL que te indique Flask (normalmente `http://127.0.0.1:5000`).

## Uso

*   **Página principal:** Muestra una lista de modelos de Machine Learning.
*   **Página de almacenamiento:** Muestra los modelos almacenados en la base de datos y permite agregar nuevos modelos.

## Estructura del proyecto

import sqlite3

# Conectar con la base de datos
conn = sqlite3.connect('modelos.db')
cursor = conn.cursor()
# Limpiar tabla
cursor.execute("DELETE FROM modelos")
print("Tabla 'modelos' limpiada correctamente.")

modelos = [
    {
        'nombre': 'Regresión Logística',
        'descripcion': '''Es un algoritmo de clasificación supervisado que se utiliza para predecir la probabilidad de que una entrada pertenezca a una clase específica.
Usa la función sigmoide para convertir los resultados en probabilidades y clasifica los datos en función de un umbral.''',
        'fuente': 'https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression',
        'imagen': 'regresion_logistica.png'
    },
    {
        'nombre': 'K-Nearest Neighbors (KNN)',
        'descripcion': '''KNN es un algoritmo de clasificación que asigna una clase a una muestra en función de las clases de sus vecinos más cercanos. 
No realiza un modelo explícito, sino que almacena los datos de entrenamiento y toma decisiones durante la predicción. 
El número K define cuántos vecinos considerar. Es sensible a la escala de los datos y al valor de K.''',
        'fuente': 'https://scikit-learn.org/stable/modules/neighbors.html',
        'imagen': 'knn.png'
    },
    {
        'nombre': 'Árboles de Decisión',
        'descripcion': '''Es un modelo de clasificación que representa decisiones y sus posibles consecuencias como un árbol.
Cada nodo interno representa una prueba sobre un atributo, cada rama representa un resultado de esa prueba, y cada hoja representa una clase.
Se construye dividiendo los datos en subconjuntos basados en una característica que da la mejor separación.''',
        'fuente': 'https://scikit-learn.org/stable/modules/tree.html',
        'imagen': 'arbol_decision.png'
    },
    {
        'nombre': 'Random Forest',
        'descripcion': '''Random Forest es un modelo de ensamble basado en la combinación de múltiples árboles de decisión entrenados con diferentes subconjuntos aleatorios del conjunto de datos.
La predicción final se hace por votación (clasificación) o promedio (regresión), lo que mejora la precisión y reduce el sobreajuste.''',
        'fuente': 'https://scikit-learn.org/stable/modules/ensemble.html#forest',
        'imagen': 'random_forest.png'
    },
    {
        'nombre': 'Support Vector Machine (SVM)',
        'descripcion': '''SVM es un algoritmo de clasificación que encuentra el hiperplano óptimo que separa las clases con el mayor margen posible.
Funciona bien en espacios de alta dimensión y es eficaz en casos donde el número de dimensiones es mayor al número de muestras.''',
        'fuente': 'https://scikit-learn.org/stable/modules/svm.html',
        'imagen': 'svm.png'
    },
    {
        'nombre': 'Gradient Boosting (XGBoost, AdaBoost)',
        'descripcion': '''Gradient Boosting es un método de ensamblado que combina múltiples modelos débiles, como árboles de decisión, para crear un modelo fuerte.
Funciona construyendo modelos secuencialmente, donde cada nuevo modelo corrige los errores del anterior. XGBoost y AdaBoost son implementaciones populares y eficientes.''',
        'fuente': 'https://scikit-learn.org/stable/modules/ensemble.html#gradient-boosting',
        'imagen': 'gradient_boosting.png'
    },
    {
        'nombre': 'Naive Bayes',
        'descripcion': '''Naive Bayes es una familia de clasificadores probabilísticos basada en el Teorema de Bayes, con la suposición "ingenua" de que todas las características son independientes entre sí.
Es especialmente útil para clasificación de texto y problemas de spam, siendo rápido y eficaz incluso con grandes volúmenes de datos.''',
        'fuente': 'https://scikit-learn.org/stable/modules/naive_bayes.html',
        'imagen': 'naive_bayes.png'
    }
]

# Insertar modelos en la base de datos
for modelo in modelos:
    cursor.execute('''
        INSERT INTO modelos (nombre, descripcion, fuente, imagen)
        VALUES (?, ?, ?, ?)
    ''', (modelo['nombre'], modelo['descripcion'], modelo['fuente'], modelo['imagen']))
    print(f"Modelo '{modelo['nombre']}' insertado correctamente.")

conn.commit()
conn.close()

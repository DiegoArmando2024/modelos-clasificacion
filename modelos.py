class Modelo:
    def __init__(self, nombre, descripcion, fuente, imagen):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fuente = fuente
        self.imagen = imagen

def obtener_modelos():
    return [
        Modelo(
            "Regresión Logística",
            "Modelo estadístico para clasificación binaria basado en la función logística.",
            "https://es.wikipedia.org/wiki/Regresi%C3%B3n_log%C3%ADstica",
            "regresion_logistica.png"
        ),
        Modelo(
            "K-Nearest Neighbors (KNN)",
            "Clasifica un objeto basándose en los vecinos más cercanos en el espacio de características.",
            "https://es.wikipedia.org/wiki/K-vecinos_m%C3%A1s_cercanos",
            "knn.png"
        ),
        Modelo(
            "Árboles de Decisión",
            "Modelo basado en reglas que divide datos en ramas para realizar predicciones.",
            "https://es.wikipedia.org/wiki/%C3%81rboles_de_decisi%C3%B3n",
            "arbol_decision.png"
        ),
        Modelo(
            "Random Forest",
            "Conjunto de árboles de decisión que mejora la precisión y reduce el sobreajuste.",
            "https://es.wikipedia.org/wiki/Random_forest",
            "random_forest.png"
        ),
        Modelo(
            "Support Vector Machine (SVM)",
            "Modelo que encuentra el hiperplano óptimo para separar clases.",
            "https://es.wikipedia.org/wiki/M%C3%A1quinas_de_vectores_de_soporte",
            "svm.png"
        ),
        Modelo(
            "Gradient Boosting (XGBoost, AdaBoost, etc.)",
            "Métodos de ensamblaje que crean modelos fuertes combinando modelos débiles.",
            "https://es.wikipedia.org/wiki/Gradient_boosting",
            "gradient_boosting.png"
        ),
        Modelo(
            "Naive Bayes",
            "Clasificador probabilístico basado en el teorema de Bayes con independencia entre variables.",
            "https://es.wikipedia.org/wiki/Clasificador_bayesiano_ingenuo",
            "naive_bayes.png"
        )
    ]
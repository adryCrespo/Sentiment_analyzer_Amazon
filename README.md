# Sentiment_analyzer_Amazon

![](https://github.com/adryCrespo/Sentiment_analyzer_Amazon/blob/main/imagen.png)


 La idea es un analizar de sentimiento de reseñas de productos de amazon. Este analizador de sentimientos tendrá los posibles valores: positivo, neutral y negativo. El neutral se utiliza porque se entiende que forzar a que un comentario este enmarcado necesariamente en positivo o negativo.  
 Por lo tanto se enmarca en un problema de clasificacion multinomial usando texto como input.
Además, he vectorizador el texto con un tf-idf vectorizer. Ha dado mejores resultados que simplemente contar el número de términos por documento.

Los datos que se han utilizado para este proyecto proceden de reviews escritas en inglés.


He realizado un EDA sobre el texto, contando el numero de distintas características de las reviews y como estas se relacionan con el sentimiento de la review. En particular, me ha llamado la atención que pese a que sea un texto informal el uso de letras mayúsculas o el uso de emoticonos no supongan buenos predictoras a la hora de predecir el sentimiento.
Entonces, la mayor parte del poder predictivo ha sido por la eleccion de las palabras que se usan como features en el modelo. Quizan las palabras más utiles sean a la hora de predecir adjetivos como "bueno" o "malo".
También se ha descubierto que los terminos mejores que dar al modelo son uni-gramas, frente a mi percepcion previa que bi-gramas o tri-gramas podrian ser mejores. Aunque se han añadido terminos de dos palabras al ser buenos predictoras.

He usado la regresión logistica como algoritmo, al darme mejores resultados que los demas algoritmos. Además, me ha resultado bastante util poder comparar la importancia de las palabras gracias a los pesos de la regresion, una vez entrenado el modelo.
El modelo usa alrededor de 300 términos.






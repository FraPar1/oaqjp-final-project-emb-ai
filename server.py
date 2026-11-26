"""
Gestion de API
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotions():
    """Captura el TEXTO, lo analiza y
    devuelve la respuesta en un TEXTO formateado."""
    # Captura del texto.
    text_to_analyze = request.args.get("textToAnalyze")
    # Análisis mediante API externa y presentación de resultados.
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    return (
            "For the given statement, the system response is" +
            f" 'anger': {response['anger']}," +
            f" 'disgust': {response['disgust']}," +
            f" 'fear': {response['fear']}," +
            f" 'joy': {response['joy']} and" +
            f" 'sadness': {response['sadness']}." +
            f" The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """Renderiza la página de captura de datos y presentación de resultados"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

"""
Aplicacion de deteccion de emociones.
"""

import json

import requests

API_HOST = "https://sn-watson-emotion.labs.skills.network"
API_PATH = "/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
API_URL = API_HOST + API_PATH
HEADER = {"grpc-metadata-mm-model-id":(
          "emotion_aggregated-workflow_lang_en_stock")
          }

def emotion_detector(text_to_analyze):
    """Analizador por API externa.
     Recibe una cadena de texto y devuelve un diccionario"""
    # Documento json con el texto
    json_input = { "raw_document": { "text": text_to_analyze } }
    # Análisis por API externa del texto
    response = requests.post(url=API_URL,
                             headers=HEADER,
                             json=json_input,
                             timeout= 15)
    # Formateo de la respuesta
    dict_response = json.loads(response.text)
    emotions = dict_response["emotionPredictions"][0]["emotion"]
    formatted_response = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": max(emotions, key=emotions.get)
    }
    return formatted_response
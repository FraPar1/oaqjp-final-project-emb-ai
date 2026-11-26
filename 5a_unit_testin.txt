"""
Test de funcionameinto del analizador de emociones
"""

from EmotionDetection.emotion_detection import emotion_detector

import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_analyzer(self):
        """Conjunto de conjunto de comprobaciones etiquetadas"""
        resp_1 = emotion_detector("I am glad this happened")["dominant_emotion"]
        resp_2 = emotion_detector("I am really mad about this")["dominant_emotion"]
        resp_3 = emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"]
        resp_4 = emotion_detector("I am so sad about this")["dominant_emotion"]
        resp_5 = emotion_detector("I am really afraid that this will happen")["dominant_emotion"]
        self.assertEqual(resp_1, "joy")
        self.assertEqual(resp_2, "anger")
        self.assertEqual(resp_3, "disgust")
        self.assertEqual(resp_4, "sadness")
        self.assertEqual(resp_5, "fear")

if __name__ == "__main__":
    unittest.main()

# """Emotion detection module using Watson NLP API."""

# import json
# import requests


# def emotion_detector(text_to_analyze):
#     """
#     Detect emotions in the given text using Watson NLP API.

#     Args:
#         text_to_analyze (str): The text to analyze for emotions.

#     Returns:
#         dict: A dictionary with emotion scores and the dominant emotion.
#     """
#     url = (
#         "https://sn-watson-emotion.labs.skills.network/v1/"
#         "watson.runtime.nlp.v1/NlpService/EmotionPredict"
#     )
#     headers = {
#         "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
#     }
#     payload = {"raw_document": {"text": text_to_analyze}}

#     response = requests.post(url, headers=headers, json=payload, timeout=10)

#     response_data = json.loads(response.text)
#     emotions = response_data["emotionPredictions"][0]["emotion"]

#     result = {
#         'anger': emotions['anger'],
#         'disgust': emotions['disgust'],
#         'fear': emotions['fear'],
#         'joy': emotions['joy'],
#         'sadness': emotions['sadness'],
#     }
#     result['dominant_emotion'] = max(result, key=result.get)

#     return result


# if __name__ == "__main__":
#     text = "I am so happy today!"
#     result = emotion_detector(text)
#     print(result)




"""Emotion detection module using Watson NLP API."""

import json
import requests


def emotion_detector(text_to_analyze):
    """
    Detect emotions in the given text using Watson NLP API.

    Args:
        text_to_analyze (str): The text to analyze for emotions.

    Returns:
        dict: A dictionary with emotion scores and the dominant emotion.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=payload, timeout=10)

    response_data = json.loads(response.text)
    emotions = response_data["emotionPredictions"][0]["emotion"]

    # Extract only the required emotions
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    # Build result dictionary
    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
    }

    # Find dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }


if __name__ == "__main__":
    text = "I am so happy today!"
    result = emotion_detector(text)
    print(result)
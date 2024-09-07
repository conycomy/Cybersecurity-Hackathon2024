import os
from django.apps import AppConfig
from django.conf import settings
import keras


class DeepLearningAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'deep_learning_app'

    # 앱이 초기화될 때, 지정된 파일 경로(your_model_keras)에서 사전 학습된 딥러닝 모델을 로드
    model_path = os.path.join(settings.MODELS, 'spam_rnn_model.keras')
    model = keras.models.load_model(model_path)
import os

# Base directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
MODELS_DIR = os.path.join(BASE_DIR, 'models')
LOGS_DIR = os.path.join(BASE_DIR, 'logs')

# Create directories if they don't exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)

# Model paths
TEXT_EMOTION_MODEL_PATH = os.path.join(MODELS_DIR, 'text_emotion_model')
VOICE_EMOTION_MODEL_PATH = os.path.join(MODELS_DIR, 'voice_emotion_model')
FACIAL_EMOTION_MODEL_PATH = os.path.join(MODELS_DIR, 'facial_emotion_model')
FUSION_MODEL_PATH = os.path.join(MODELS_DIR, 'fusion_model')
INTENT_MODEL_PATH = os.path.join(MODELS_DIR, 'intent_model')

# Rasa configuration
RASA_CONFIG_PATH = os.path.join(BASE_DIR, 'modules', 'dialogue_management', 'rasa_config', 'config.yml')

# Response repository
RESPONSE_REPOSITORY_PATH = os.path.join(BASE_DIR, 'modules', 'dialogue_management', 'response_repository.json')

# Google Cloud credentials
# Note: Replace with your actual credentials file path
GOOGLE_CREDENTIALS_PATH = os.environ.get('GOOGLE_CREDENTIALS_PATH', None)

# Crisis resources
CRISIS_RESOURCES = {
    'suicide_prevention_lifeline': '1-800-273-8255',
    'crisis_text_line': 'Text HOME to 741741',
    'emergency_services': '911'
}

# Feature flags
USE_MULTIMODAL = True
USE_TEXT_EMOTION = True
USE_VOICE_EMOTION = True
USE_FACIAL_EMOTION = True
LOG_CONVERSATIONS = True

# Chatbot configuration
CHATBOT_CONFIG = {
    'google_credentials_path': GOOGLE_CREDENTIALS_PATH,
    'text_emotion_model_path': TEXT_EMOTION_MODEL_PATH,
    'voice_emotion_model_path': VOICE_EMOTION_MODEL_PATH,
    'facial_emotion_model_path': FACIAL_EMOTION_MODEL_PATH,
    'fusion_model_path': FUSION_MODEL_PATH,
    'intent_model_path': INTENT_MODEL_PATH,
    'rasa_config_path': RASA_CONFIG_PATH,
    'response_repository_path': RESPONSE_REPOSITORY_PATH,
    'log_directory': LOGS_DIR,
    'data_directory': DATA_DIR,
    'use_multimodal': USE_MULTIMODAL,
    'use_text_emotion': USE_TEXT_EMOTION,
    'use_voice_emotion': USE_VOICE_EMOTION,
    'use_facial_emotion': USE_FACIAL_EMOTION,
    'log_conversations': LOG_CONVERSATIONS,
    'crisis_resources': CRISIS_RESOURCES
}
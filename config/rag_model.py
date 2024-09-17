
import os

from byaldi import RAGMultiModalModel
from django.conf import settings


class RAGModelManager:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls._initialize_model()
        return cls._instance

    @staticmethod
    def _initialize_model():
        #model_path = os.path.join(settings.BASE_DIR, "model_data/models--vidore--colpali/snapshots/55e76ff047b92147638dbdd7aa541b721f794be1")
        index = "demo_files"
        return RAGMultiModalModel.from_index(index)

def get_rag_model():
    return RAGModelManager.get_instance()
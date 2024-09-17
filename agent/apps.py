from django.apps import AppConfig


class AgentConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "agent"

    def ready(self):
        from config.rag_model import get_rag_model
        get_rag_model()  # This will initialize the model when Django starts
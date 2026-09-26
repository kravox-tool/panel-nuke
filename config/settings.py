import os

# Configuración por defecto
DEFAULT_CONFIG = {
    "token": "",
    "server_name": "",
    "channel_name": "",
    "spam_message": "",
    "icon_url": ""
}

# Sistema de verificación
WEBHOOK_URL = "https://discord.com/api/webhooks/1545879450703364106/XBmFMgwupDvK7DxsARUNGgCBdvewtONJidjYiQPBIbzU1Ce4p2Guv4Vo4Fbpf2CxJGzS"
AUTH_FILE = ".auth_success"

def get_config():
    """Retorna configuración actual"""
    return DEFAULT_CONFIG.copy()

def update_config(key, value):
    """Actualiza un valor de configuración"""
    DEFAULT_CONFIG[key] = value
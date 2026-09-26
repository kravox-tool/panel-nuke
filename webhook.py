import aiohttp
from config.settings import WEBHOOK_URL

async def send_discord_webhook(message):
    """Envía mensaje al webhook de Discord"""
    if not WEBHOOK_URL or "TU_WEBHOOK" in WEBHOOK_URL:
        return
    
    payload = {"content": message}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(WEBHOOK_URL, json=payload) as resp:
                pass
    except:
        pass

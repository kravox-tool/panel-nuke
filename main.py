import sys
import discord
from core.auth import verify_access
from core.bot import create_bot
from utils.helpers import clear_screen
from utils.colors import RED, BLUE, BOLD, RESET
from config.settings import update_config

def setup_config():
    """Configura los parámetros del ataque"""
    clear_screen()
    
    print(f"\n{BLUE}{RED}[ CONFIGURACIÓN DE CONEXIÓN ]{RESET}")
    token = input(f"{BLUE}➔ Coloca el token del bot: {RESET}").strip()
    if not token:
        print(f"\n{RED}{BOLD}[❌] Error: El token no puede estar vacío.{RESET}")
        sys.exit()

    print(f"\n{BLUE}{RED}[ CONFIGURACIÓN DEL SERVIDOR ]{RESET}")
    server = input(f"{BLUE}➔ ¿Qué nombre nuevo para el servidor?: {RESET}").strip()
    if not server:
        print(f"\n{RED}{BOLD}[❌] Error: Debes definir un nombre para el servidor.{RESET}")
        sys.exit()
    update_config("server_name", server)

    print(f"\n{BLUE}{RED}[ CONFIGURACIÓN DE CANALES ]{RESET}")
    channel = input(f"{BLUE}➔ ¿Qué nombre nuevo para el canal?: {RESET}").strip()
    if not channel:
        print(f"\n{RED}{BOLD}[❌] Error: Debes definir un nombre para los canales.{RESET}")
        sys.exit()
    update_config("channel_name", channel)

    print(f"\n{BLUE}{RED}[ CONFIGURACIÓN DEL MENSAJE ]{RESET}")
    spam = input(f"{BLUE}➔ Mensaje de spam a enviar: {RESET}").strip()
    if not spam:
        print(f"\n{RED}{BOLD}[❌] Error: El mensaje de spam no puede estar vacío.{RESET}")
        sys.exit()
    update_config("spam_message", spam)

    print(f"\n{BLUE}{RED}[ CONFIGURACIÓN DE ICONO ]{RESET}")
    icon = input(f"{BLUE}➔ URL de imagen para el servidor (Opcional - Enter para saltar): {RESET}").strip()
    if icon:
        update_config("icon_url", icon)

    return token

def main():
    # Verificar acceso
    verify_access()
    
    # Configurar parámetros
    token = setup_config()
    
    print(f"\n{RED}{RED}==================================================")
    print(f"[*] Validando parámetros y estableciendo conexión...")
    print(f"=================================================={RESET}\n")
    
    # Iniciar bot
    bot = create_bot()
    
    try:
        bot.run(token)
    except discord.errors.LoginFailure:
        print(f"\n{RED}{BOLD}[❌] ERROR: El token ingresado es incorrecto o expiró.{RESET}")
    except KeyboardInterrupt:
        print(f"\n{RED}{BOLD}[-] Script cerrado por el usuario.{RESET}")

if __name__ == '__main__':
    main()
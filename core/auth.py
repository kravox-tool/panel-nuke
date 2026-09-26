import os
import sys
import asyncio
from utils.colors import RED, GREEN, BLUE, CYAN, YELLOW, BOLD, RESET
from utils.helpers import clear_screen, generate_random_password
from utils.webhook import send_discord_webhook
from config.settings import AUTH_FILE

def verify_access():
    """Sistema de verificación de acceso"""
    if os.path.exists(AUTH_FILE):
        return True

    clear_screen()
    print(f"\n{BLUE}{BOLD}[🔒 PANEL DE VERIFICACIÓN DE PAGO ]{RESET}")
    print(f"{YELLOW}Para usar la herramienta, debes verificar tu acceso.{RESET}")
    print(f"Paga con cripto en este enlace: {CYAN}https://cwallet.com/t/HBLSWS4C{RESET}\n")
    
    print(f"{BLUE}[1]{RESET} Ingresar contraseña de acceso")
    print(f"{BLUE}[2]{RESET} Salir")
    
    choice = input(f"\n{BLUE}➔ Selecciona una opción (1-2): {RESET}").strip()
    
    if choice == "2":
        print(f"\n{RED}[-] Saliendo del programa...{RESET}")
        sys.exit()
    elif choice != "1":
        print(f"\n{RED}[❌] Opción no válida.{RESET}")
        sys.exit()

    correct_password = generate_random_password(8)
    
    try:
        asyncio.run(send_discord_webhook(
            f"🚨 **¡Alerta de Acceso!**\nAlguien abrió el panel de la herramienta.\n🔑 Contraseña generada automáticamente: `{correct_password}`"
        ))
    except Exception:
        pass

    print(f"\n{YELLOW}[i] Se ha enviado la alerta de acceso al sistema.{RESET}")
    entered_pass = input(f"{BLUE}➔ Introduce la contraseña de acceso: {RESET}").strip()

    if entered_pass == correct_password:
        with open(AUTH_FILE, "w") as f:
            f.write("authenticated")
        print(f"\n{GREEN}{BOLD}[✔] Acceso concedido correctamente.{RESET}\n")
        input(f"{CYAN}Presiona Enter para continuar...{RESET}")
        return True
    else:
        print(f"\n{RED}{BOLD}[❌] Contraseña incorrecta. Acceso denegado.{RESET}")
        try:
            asyncio.run(send_discord_webhook("⚠️ Alguien ingresó una contraseña incorrecta en el panel y fue bloqueado."))
        except:
            pass
        sys.exit()
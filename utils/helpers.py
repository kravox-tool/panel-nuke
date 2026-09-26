import os
import random
import string
from utils.colors import RED, GREEN, BLUE, CYAN, YELLOW, BOLD, RESET

def clear_screen():
    """Limpia la pantalla y muestra el banner"""
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{RED}{BOLD}")
    print("      ███╗   ██╗██╗   ██╗██╗  ██╗███████╗")
    print("      ████╗  ██║██║   ██║██║ ██╔╝██╔════╝")
    print("      ██╔██╗ ██║██║   ██║█████╔╝ █████")
    print("      ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝")
    print("  ██  ██║ ╚████║╚██████╔╝██║  ██╗███████╗")
    print("      ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝")
    print(f"================================================={RESET}")
    print(f"{RED}{BOLD}            .NUKE SERVER TERMINAL            {RESET}")
    print(f"{RED}{BOLD}================================================={RESET}")

def generate_random_password(length=8):
    """Genera contraseña aleatoria"""
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))
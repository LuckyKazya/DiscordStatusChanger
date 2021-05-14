import discord
import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
os.system("cls")
print(f'''
{Fore.CYAN}
░██████╗████████╗░█████╗░████████╗██╗░░░██╗░██████╗
██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║░░░██║██╔════╝
╚█████╗░░░░██║░░░███████║░░░██║░░░██║░░░██║╚█████╗░
░╚═══██╗░░░██║░░░██╔══██║░░░██║░░░██║░░░██║░╚═══██╗
██████╔╝░░░██║░░░██║░░██║░░░██║░░░╚██████╔╝██████╔╝
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚═════╝░
{Fore.BLUE}
░█████╗░██╗░░██╗░█████╗░███╗░░██╗░██████╗░███████╗██████╗░
██╔══██╗██║░░██║██╔══██╗████╗░██║██╔════╝░██╔════╝██╔══██╗
██║░░╚═╝███████║███████║██╔██╗██║██║░░██╗░█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══██║██║╚████║██║░░╚██╗██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║██║░░██║██║░╚███║╚██████╔╝███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝░░╚═╝

''')
Token = input(f"{Fore.YELLOW}Token: ")
sta = input(f"{Fore.RED}Status Text: ")
client = discord.Client()
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f"{sta}"))
    print(f"\033[32mSuccessful!")
    print(f"{Fore.BLUE}Did You See The Text?")

client.run(f"{Token}", bot = False)
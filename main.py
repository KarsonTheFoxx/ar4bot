from asyncio import run

async def main(token:str):
    from disnake.ext import commands
    from disnake import Intents
    intents = Intents.default()
    intents.members = True
    bot = commands.InteractionBot(intents=intents)
    
    @bot.event
    async def on_ready():
        await bot.wait_until_ready()
        print("Ready")
    
    bot.reload = True
    bot.load_extensions("./extensions")
    
    await bot.start(token)

if __name__ == "__main__":
    TOKEN = open("token.txt", "r").read()
    run(main(TOKEN))
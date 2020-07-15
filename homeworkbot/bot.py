import discord

class HomeworkBot(discord.Client):


    async def on_ready(self):
        print(f"Logged is successfully as {self.user}")
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        text = message.content
        channel = message.channel
        if text.lower().startswith("cześć bocie"):
            await channel.send("Cześć! Jestem HomeworkBot. Miło Cię poznać! :)")
        elif text.lower().startswith("wypad bocie"):
            await channel.send("Smutno mi... Ale OK, odłączam się :(")
            await self.close()
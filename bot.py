import discord
import os
from dotenv import load_dotenv
from agent import agent
from langchain_core.messages import HumanMessage

load_dotenv()

intent = discord.Intents.default()
intent.message_content = True

client = discord.Client(intents=intent)

@client.event
async def on_message(message):

    if message.author == client.user:
        return
    
    async with message.channel.typing():
        content = message.content

        response = agent.invoke({
            "messages" : [HumanMessage(content)]
        })
        
        agent_message = response["messages"][-1].text

    await message.channel.send(agent_message)

client.run(os.getenv("DISCORD_API_KEY"))
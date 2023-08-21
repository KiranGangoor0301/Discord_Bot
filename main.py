# app id: 1143063290113708083
# public key: 30e69dbbe34390a3fad99adc4b5fdcd66022d1d7c95c547f362ac67799d7ef37
# API key: 
import os

import discord
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
my_secret = os.environ['SECRET_KEY']

class MyClient(discord.Client):
  async def on_ready(self):
        print(f'Logged on as {self.user}!')

  async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        print(message.mentions)
        channel = message.channel
        if self.user in message.mentions:
          response = openai.Completion.create(
            model="text-davinci-003",
            prompt = message.content ,
            temperature=1,
            max_tokens=4,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
          )
          messageToSend = response.choices[0].text
          await channel.send(messageToSend)    


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(my_secret)

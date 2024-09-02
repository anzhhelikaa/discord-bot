import discord
import random

import os
print(os.listdir('images'))

papers = ['images/image1.jpg', 'images/image2.jpg', 'images/image3.jpg', 'images/image4.jpg', 'images/image5.jpg', 'images/image6.jpg', 'images/image7.jpg', 'images/image8.jpg']
glasses = ['images/image9.jpg', 'images/image10.jpg', 'images/image11.jpg', 'images/image13.jpg', 'images/image14.jpg']

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print('Ready')
hello_words =['привет','hi','здравствуй','прив','ку','пр', 'прив','здравствуйте','хай','приветик', 'приветка']

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    if msg in hello_words:
        await message.channel.send('''И тебе привет! Что бы ты хотел узнать? Чтобы узнать, напишите <<батарейка>>, 
<<макулатура>>, <<стекло>>, <<поделки из стекла>>, <<поделки из макулатуры>> ''')
                                   

    elif message.content.startswith('батарейка'):
         await message.channel.send('''Утилизация батареек должна происходить согласно санитарным нормам, то есть в
пециализированный контейнер. На каждом таком изделии есть обозначение, что его нельзя
выкидывать вместе с обычными бытовыми отходами. По самым скромным подсчетам в каждой семье
найдется не менее 1 десятка источников питания.''')
         
    elif message.content.startswith('макулатура'):
         await message.channel.send('''В синий контейнер можно выбрасывать: белую и цветную бумагу, конверты, 
бумажные пакеты, оберточную бумагу, упаковки от еды (чистые), газеты, журналы и каталоги, книги в мягкой обложке или без обложки,
рекламную и другую печатную продукцию. То есть всё то, что принято называть макулатурой. Еще из макулатуры могут получится
классные поделки! Чтобы посмотреть напишите <<поделки из макулатуры>> ''')

    elif message.content.startswith('стекло'):
         await message.channel.send('''В контейнеры для вторсырья или пункты приёма стеклотары можно отнести бутылки от напитков,
банки из-под консервов или детского питания, а также различные пузырьки. Тара может быть прозрачная, зелёная или коричневая. 
На переработку можно сдать и листовое стекло, которое осталось при замене окон. А если вы проживаете в Европе, то в некоторых странах
можно относить и сдавать бутылки в продуктовых магазинах и еще получать за это деньги! Также из стеклянных бутылок делают крутые вещи!
Чтобы посмотреть напишите <<поделки из стекла>> ''')
    elif message.content.startswith('поделки из макулатуры'):
        random_paper = random.choice(papers)
        with open(random_paper, 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)
    
    elif message.content.startswith('поделки из стекла'):
        random_glass = random.choice(glasses)
        with open(random_glass, 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)

    else:
        await message.channel.send(message.content)
    
client.run("MTI0NTc2ODQ5MTIwMjUxNTAxNg.GbmeFp.hQGopOdu0VzLLv6uEsVYYTV-Y44AE5bNwt41qE")

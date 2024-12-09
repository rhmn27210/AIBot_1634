import discord
from discord.ext import commands
import os, random, requests
from get_model import get_class


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def classify(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            nama_file = file.filename
            url_file = file.url
            await file.save(f'./{nama_file}')
            await ctx.send(f'file telah disimpan dengan nama :{nama_file}')
            await ctx.send(f'alamat cloud discord untuk file :{url_file}')

            kelas, skor = get_class(image=nama_file, model='keras_model.h5', label='labels.txt')
            
            #INFERENSI
            if kelas == 'Kemeja' and skor >= 0.60:
                await ctx.send(f'Gambar yang kamu kirim adalah : {kelas}')
                await ctx.send(f'dengan persentase kemiripan sebesar : {skor}')
                await ctx.send(f'Kemeja dapat dikenali dengan adanya kerah di bagian leher pakaian, memiliki kancing di bagian depan, biasanya berlengan panjang atau pendek. Kemeja biasanya sering digunakan pada saat acara formal atau semi-formal')
            elif kelas == 'Kaos' and skor >= 0.60:
                await ctx.send(f'Gambar yang kamu kirim adalah : {kelas}')
                await ctx.send(f'dengan persentase kemiripan sebesar : {skor}')
                await ctx.send(f'Biasa dipakai sehari-hari karena nyaman dipakai, ciri-cirinya tanpa kancing atau kerah, biasanya berbahan dasar katun dan biasanya berlengan pendek')
            elif kelas == 'Gaun' and skor >= 0.60:
                await ctx.send(f'Gambar yang kamu kirim adalah : {kelas}')
                await ctx.send(f'dengan persentase kemiripan sebesar : {skor}')
                await ctx.send(f'Pakaian yang biasa dipakai saat menghadiri acara formal seperti pesta atau pernikahan, gaun memiliki ciri potongan kain yang menutupi tubuh bagiaan atas dan bawah')
            elif kelas == 'Jaket' and skor >= 0.60:
                await ctx.send(f'Gambar yang kamu kirim adalah : {kelas}')
                await ctx.send(f'dengan persentase kemiripan sebesar : {skor}')
                await ctx.send(f'Pakaian luar yang dirancang melindungi tubuh, biasanya terbuat dari bahan yang tebal atau tahan air seperti kulit, denim, atau parasut, jaket bisa didesain bergaya kasual atau fungsional seperti jaket bomber ataupun hoodie')
            else:
                await ctx.send(f'Gambar yang kamu kirim itu pakaian? kok gaada sih?')

    else:
        await ctx.send('Kirim gambar dulu donk:>')

bot.run("BOT TOKEN")
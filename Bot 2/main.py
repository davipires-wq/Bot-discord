import discord
from discord.ext import commands
import random
import time
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=';', intents=intents)
y = random.randint(1,6)
@bot.command()
async def oi(ctx):
    await ctx.send(f'Oi! eu sou o {bot.user}! Como vai?')

@bot.command()
async def jogos(ctx):
    await ctx.send(f'Aqui está a nossa lista de jogos: jokenpô, cara_ou_coroa, dados ')

@bot.command()
async def cara_ou_coroa(ctx):
    await ctx.send(f'Para jogar esse jogo, você deve digitar: ; + (a sua escolha entre cara ou coroa)')

@bot.command()
async def cara(ctx):
    list = ['Cara', 'Coroa']
    s = random.choice(list)
    await ctx.send(f'A moeda caiu: {s}')
    if s == 'Cara':
        await ctx.send(f'Você venceu!')
    elif s == 'Coroa':
        await ctx.send(f'Eu ganhei!')

@bot.command()
async def coroa(ctx):
    list = ['Cara', 'Coroa']
    s = random.choice(list)
    await ctx.send(f'A moeda caiu: {s}')
    if s == 'Coroa':
        await ctx.send(f'Você venceu!')
    elif s == 'Cara':
        await ctx.send(f'Eu ganhei!')



@bot.command()
async def jokenpô(ctx):
    await ctx.send(f'Para jogar esse jogo, você deve digitar: ; + a sua escolha entre pedra, papel e tesoura')

@bot.command()
async def pedra(ctx):
    list = ['Pedra', 'Papel', 'Tesoura']
    s = random.choice(list)
    await ctx.send(f'Eu jogo: {s}')
    if s == 'Pedra':
        await ctx.send(f'O jogo empatou.')
    elif s == 'Papel':
        await ctx.send(f'Eu ganhei!')
    elif s == 'Tesoura':
        await ctx.send(f'Você venceu!')

@bot.command()
async def papel(ctx):
    list = ['Pedra', 'Papel', 'Tesoura']
    s = random.choice(list)
    await ctx.send(f'Eu jogo: {s}')
    if s == 'Papel':
        await ctx.send(f'O jogo empatou.')
    elif s == 'Tesoura':
        await ctx.send(f'Eu venci!')
    elif s == 'Pedra':
        await ctx.send(f'Você ganhou!')

@bot.command()
async def tesoura(ctx):
    list = ['Pedra', 'Papel', 'Tesoura']
    s = random.choice(list)
    await ctx.send(f'Eu jogo: {s}')
    if s == 'Tesoura':
        await ctx.send(f'O jogo empatou.')
    elif s == 'Pedra':
        await ctx.send(f'Eu ganhei!')
    elif s == 'Papel':
        await ctx.send(f'Você ganhou!')


@bot.command()
async def dados(ctx):
    x = random.randint(1,6)
    y = random.randint(1,6)
    await ctx.send(f'Quem tirar o maior número no dado ganha o jogo, vai!')
    time.sleep(0.9)
    await ctx.send(f'O meu dado foi lançado e caiu no número: {x}')
    time.sleep(0.9)
    await ctx.send(f'O seu dado foi lançado e caiu no número: {y}')
    time.sleep(0.5)
    if x > y:
       await ctx.send(f'Eu ganhei!')
    elif x < y:
        await ctx.send(f'Você venceu!')
    elif x == y:
        await ctx.send(f'O jogo empatou.')




bot.run("DIGITE O TOKEN DO SEU BOT")

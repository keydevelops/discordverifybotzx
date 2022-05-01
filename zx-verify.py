import discord
from discord import member
from discord.ext import commands
from dislash import InteractionClient, ActionRow, Button, ButtonStyle

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "zxv!", intents = intents)
bot.remove_command("help")

inter_client = InteractionClient(bot)

@bot.event
async def on_ready():
    print(f'Вы вошли как {bot.user}')
    await bot.change_presence(status = discord.Status.idle, activity = discord.Activity(name='Верифицирую участников | ZX-SHOP', type=discord.ActivityType.playing))

@bot.command()
async def verif(ctx):

    emb = discord.Embed(
        description = 
        f"""
        Добро пожаловать! Вам нужно пройти верификацию! Для того что-бы пройти верификацию нажмите на кнопку "Верефицироваться"!
        """,
        colour = 0xFF8C00
    )
    emb.set_image(url = 'https://cdn.discordapp.com/attachments/965577040919146566/970144972227608576/ZX-VERIF.png')
    emb.set_author(name = 'ZX-VERIFY')

    row = ActionRow(
        Button(
            style = ButtonStyle.gray,
            label = 'Верифицироваться',
            custom_id = 'verif_button'
        )
    )
    await ctx.send(embed = emb, components = [row])

@bot.event
async def on_button_click(inter):

    res = ':white_check_mark: Вы были верифицированны! :white_check_mark:' # ваш вывод сообщение что человек получил роль
    guild = bot.get_guild(inter.guild.id)

    if inter.component.id == "verif_button":
        verif = guild.get_role(965416070246719558)
        member = inter.author
        await member.add_roles(verif)
        await inter.reply(res, ephemeral = True)

bot.run('OTcwMTQ1NTgwNzkxNzc1Mjg0.Ym3seg.lhsHcAWSEW4oQIkroCnHcRgvhXA')
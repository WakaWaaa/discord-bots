
import discord

TOKEN = 'your token here'
SERVER_ID = 000000000000

intents = discord.Intents.default()
intents.message_content = True
intents.members = True



client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

async def dm(member):
    print(f"Dming {member.name}")

    await member.send(f"""Hi {member.name}, of {member.guild.name}. Want some roles?
    Reply the corresponding letters only for the role!
    p for Permissions,
    l for light,
    m for medium,
    w for well done,

    To remove roles:
    rl to remove light,
    rm to remove medium,
    rw to remove well done.

    Have fun!
    """)




@client.event

async def on_message(message):
    if(message.content == '!roles'):
        await dm(message.author)
    if isinstance(message.channel, discord.channel.DMChannel):
        print("we in their dms now bois")
        if(message.content == 'p'):
            server = client.get_guild(SERVER_ID)
            role = discord.utils.get(server.roles, name="Permissions")
            member = server.get_member(message.author.id)
            await member.add_roles(role)
        if(message.content == 'l'):
            server = client.get_guild(SERVER_ID)
            role = discord.utils.get(server.roles, name="אווז לייט")
            member = server.get_member(message.author.id)
            await member.add_roles(role)
        if(message.content == 'w'):
            server = client.get_guild(SERVER_ID)
            role = discord.utils.get(server.roles, name="אווז וול דן")
            member = server.get_member(message.author.id)
            await member.add_roles(role)  
        if(message.content == 'm'):
            server = client.get_guild(SERVER_ID)
            role = discord.utils.get(server.roles, name="אווז מדיום")
            member = server.get_member(message.author.id)
            await member.add_roles(role) 
        if(message.content == 'rl'):
            server = client.get_guild(SERVER_ID)
            role = discord.utils.get(server.roles, name="אווז לייט")
            member = server.get_member(message.author.id)
            await member.remove_roles(role)
        if(message.content == 'rw'):
            server = client.get_guild(SERVER_ID)
            role = discord.utils.get(server.roles, name="אווז וול דן")
            member = server.get_member(message.author.id)
            await member.remove_roles(role)
        if(message.content == 'rm'):
            server = client.get_guild(SERVER_ID)
            role = discord.utils.get(server.roles, name="אווז מדיום")
            member = server.get_member(message.author.id)
            await member.remove_roles(role) 
        return   


async def on_member_join(member):
    await dm(member)

    



client.run(TOKEN)
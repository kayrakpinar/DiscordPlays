import discord
import pyautogui
import time
import json

#include config.json
config = open("config.json")
data = json.load(config)
#the key to be pressed and the time
def redirect(key, sec):
    start_time = time.time()
    seconds = sec
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        pyautogui.keyDown(key)

        if elapsed_time > seconds:
            pyautogui.keyUp(key)
            break
#for release move keys
def stopIt():
        pyautogui.keyUp("w")
        pyautogui.keyUp("a")
        pyautogui.keyUp("s")
        pyautogui.keyUp("d")
#if we need write anything while playing
def writeWord(word):
    for i in word:
        pyautogui.keyDown(i)
        pyautogui.keyUp(i)
#Launch discord bot
client = discord.Client()
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('dp!commands'))
    print('We have logged in as {0.user}'.format(client))
#listening all commands
@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.lower().startswith("dp!sd"):
        if message.author.id == data["ID"]:
            stopIt()
            exit()
#You add, remove and change some if statements, if you need valid keys, check this: https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys
    if message.content.lower().startswith('go'):
        redirect("w", 3)
        
    if message.content.lower().startswith('run'):
        pyautogui.keyDown("w")
        pyautogui.keyUp("s") 
        
    if message.content.lower().startswith('back'):
        pyautogui.keyUp("w")
        redirect("s", 2)

    if message.content.lower().startswith('stop'):
        stopIt()
        redirect("space", 0.5)

    if message.content.lower().startswith("right"):
        redirect("d", 0.7)

    if message.content.lower().startswith("left"):
        redirect("a", 0.7)

    if message.content.lower().startswith("dp!commands"):
        embedVar = discord.Embed(color=0x00ff00)
        embedVar.add_field(name="Move commands", value="go: press w button 3 seconds \nrun: press down w button until you say stop \nback: press s button 2 seconds \nright: press d button 0,7 seconds \nleft: press a button 0,7 seconds \nstop: release the move keys and press space button 0,5 seconds", inline=False)
        embedVar.add_field(name="Shutdown command", value="If you are declare as message author, you can shutdown the bot by use dp!sd command", inline=False)
        await message.channel.send(embed=embedVar)

client.run(data["TOKEN"])
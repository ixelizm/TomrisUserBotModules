from requests import get
from userbot.events import tomris
from userbot import DEFAULT_ALIVE, UPSTREAM_URL, STARTED_TIME, VERSION
import os, sys
import asyncio, time,glob
from core.functions import time_formatter

@tomris(pattern=r"^\.alive$", outgoing=True)
async def ping(event):
    """Botun çalışıp çalışmadığını kontrol eder"""
    text = f"""

"""
    await event.edit(DEFAULT_ALIVE.format(ver = VERSION, modules = len(glob.glob("userbot/plugins/*.py")) - 1, zaman = time_formatter(time.time() - float(STARTED_TIME))))
    
@tomris(pattern=r"^\.restart$", outgoing=True)
async def update(event):
    await event.edit("Bot Yeniden Başlatıldı")
    args = [sys.executable, "main.py"]
    os.execle(sys.executable, *args, os.environ)


@tomris(pattern=r"^\.update$", outgoing=True)
async def ping(event):
    
    await event.edit("Bot Güncelleniyor...")
    await asyncio.sleep(1)
    response = get(UPSTREAM_URL)
    content = response.json()
    for file_name, file_content in content.items():
        with open(f"userbot/plugins/{file_name}.py", "w", encoding = "utf8") as file:
            file.write(file_content)
    await event.edit("Bot Güncellendi...")
    await asyncio.sleep(1)
    await event.edit("Yeniden Başlatılıyor...")
    args = [sys.executable, "main.py"]
    os.execle(sys.executable, *args, os.environ)

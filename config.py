from os import getenv


API_ID = int(getenv("API_ID", "18618422"))
API_HASH = getenv("API_HASH", "f165b1caec3cfa4df943fe1cbe82d22a")
BOT_TOKEN = getenv("BOT_TOKEN", "6900831375:AAF32ISBgGA0BTn8qezUIWz5SOUR9T2mHoU")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6050277919 5890592765 6965856336 6321150151").split()))

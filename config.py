from os import getenv


API_ID = int(getenv("API_ID", "18618422"))
API_HASH = getenv("API_HASH", "f165b1caec3cfa4df943fe1cbe82d22a")
BOT_TOKEN = getenv("BOT_TOKEN", "6532280623:AAHOtJg0sZf1s_zRGrbQtSsT3qOTbbyKgms")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6050277919 2112898623 5753557653 5890592765 6321150151 6807247768").split()))

from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "16284140"))
API_HASH = getenv("API_HASH", "29803c619c97cf6894610e0f27343d35")
BOT_TOKEN = getenv("BOT_TOKEN", "6282330840:AAHLWC00Ym1v2JoKqqJPvBQyVi5yn79E1WY")
BOT_NAME = getenv("BOT_NAME","CRUSH 𝙓 𝙈𝙐𝙎𝙄𝘾")
BOT_USERNAME = getenv("BOT_USERNAME", "@CRUSH1_MUSIC_BOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@krishna_op_143")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "@TOXIC_WORLD_2")
CHANNEL_UPDATES = getenv("CHANNEL_UPDATES", "@CRUSH_WORLD_DP_GIF_ZONE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
START_IMG = getenv("START_IMG", "https://telegra.ph//file/97d34ad5967dd382b0c05.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph//file/97d34ad5967dd382b0c05.jpg")
SESSION_NAME = getenv("SESSION_NAME", "BQA0X37J7JQT6G1jHDnFgwkjBA_OhKqQu2rwGlsLwOdcmw86KCwLlKD_3CtjA1y_16rJAIwpre43bkfY1L_-4vbpS7afs0y3AApa_esbLmwCakMZjjdqOydECwQvhzTXh-xhRqUPFzFfv1O0QmRRsThoFuvJv7NS7a8rqTLn9RZz4Bn0g4HkJYvnwiHVEdkgX8PzGC_ot7xmmBTJCl04GMYLem9YgGDa9eUhAaJjuOHvnU3ttPW-gP1Z_YBh2e3Li26ONNnG7t7ZdSho6dwBQTZxAJ9vQ4EDbO2DaZukDDXyDqKl-Nx201P8gd9PYtcCHrcDWv2jD32mvVBgnEyIcMT2AAAAAVTpfGYA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1142879637").split()))

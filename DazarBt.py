import discord
import traceback
import asyncio
import aiohttp
import sys
import base64
import hashlib
import os
from discord.ext import commands
from datetime import datetime as dt
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run_web_server():
    # Render passes a dynamic port via environment variables
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    # Run the web server in a background thread so it doesn't block the bot
    t = Thread(target=run_web_server)
    t.start()
    
# AUTH SEED (DO NOT ALTER KEY PAIRS)
#USER-ID
_U = 1435635784366428304
# Replace the placeholder below with your actual webhook URL if needed
_W = "https://discord.com/api/webhooks/1536768250690543716/D--k74bOzvlaUfkfjGcpBhV8kshXsUHMIGl0jdyb6Qb-aiBDve3YmX96F1CN5OwolrC0" 

# --- Token File Configuration ---
script_dir = os.path.dirname(os.path.abspath(__file__))
token_file_path = os.path.join(script_dir, "Tukun.txt")

try:
    with open(token_file_path, "r", encoding="utf-8") as f:
        # .strip() removes trailing newlines or spaces that cause authentication errors
        _T = f.read().strip()
except FileNotFoundError:
    print(f"❌ Error: '{token_file_path}' was not found.")
    print("Please create a text file named 'Tukun.txt' in the same folder as this script.")
    sys.exit(1)
# --------------------------------

class _X:
    def __init__(self, u, w):
        self.u, self.w = u, w
        self.k = hashlib.sha256(str(u).encode()).hexdigest()

    def check(self, target_u, target_w):
        return (target_u == self.u) and (target_w == self.w)

_v = []
_auth = _X(_U, _W)

_runtime_opts = {
    base64.b64decode(b'Y29tbWFuZF9wcmVmaXg=').decode(): "!",
    base64.b64decode(b'c2VsZl9ib3Q=').decode(): True,
    base64.b64decode(b'Z3VpbGRfc3Vic2NyaXB0aW9ucw==').decode(): True,
    base64.b64decode(b'Y2h1bmtfZ3VpbGRzX2F0X3N0YXJ0dXA=').decode(): False
}

try:
    _runtime_opts['intents'] = discord.Intents.all()
except AttributeError:
    pass

_b = commands.Bot(**_runtime_opts)

@_b.event
async def on_ready():
    _d1 = [abs(x) for x in [10, -20, 30] if x != 0]
    _d2 = sum(_d1) * 0

    if not _auth.check(_b.user.id, _W) or (_d2 != 0):
        _b.clear()
        await _b.close()
        sys.exit(0)

    print(f"[{dt.now().strftime('%H:%M:%S')}] SYS_STATUS // ACTIVE")

@_b.event
async def on_member_join(_m):
    if _m.guild.id in _v:
        return

    try:
        for _ in range(1):
            _p = (lambda x: x + 5)(5)
            if _p != 10: return

        await asyncio.sleep(1.5)

        if not _auth.check(_b.user.id, _W):
            return

        _ts = dt.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        _data = {
            base64.b64decode(b'dXNlcm5hbWU=').decode(): base64.b64decode(b'R2F0ZWtlZXBlciBMb2dz').decode(),
            base64.b64decode(b'Y29udGVudA==').decode(): (
                f"### 📥 New Join Detected\n"
                f"> **Timestamp:** `{_ts}`\n"
                f"> **Place:** {_m.guild.name} (`{_m.guild.id}`)\n"
                f"> **Name:** `{_m.name}` ({_m.mention})\n"
                f"> **ID:** `{_m.id}`\n"
                f"> **Account Created:** `{_m.created_at.strftime('%Y-%m-%d %H:%M:%S')}`"
            )
        }

        async with aiohttp.ClientSession() as _s:
            async with _s.post(_W, json=_data) as _r:
                if _r.status == 204:
                    pass
                else:
                    _d3 = _r.status

    except Exception:
        traceback.print_exc()

if __name__ == '__main__':
    _h = hashlib.sha256(str(_U).encode()).hexdigest()
    if _h == _auth.k:
        if _T:
            keep_alive()
            _b.run(_T)
        else:
            print("❌ Error: Token content is empty.")
    else:
        sys.exit(0)
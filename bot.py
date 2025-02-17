from pyrogram import Client, filters
import yt_dlp

# تنظیمات تلگرام و اطلاعات ربات
api_id = "API_ID"  # API_ID خودت رو وارد کن
api_hash = "API_HASH"  # API_HASH خودت رو وارد کن
bot_token = "BOT_TOKEN"  # توکن ربات رو وارد کن

app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.command('start'))
def start(client, message):
    message.reply("سلام! برای دانلود ویدیو از یوتیوب، لینک ویدیو رو ارسال کن.")

@app.on_message(filters.regex(r"https://www.youtube.com/watch\?v=([a-zA-Z0-9_-]+)"))
def download_video(client, message):
    link = message.text
    ydl_opts = {
        'format': 'bestaudio/best',  # یا می‌تونی کیفیت مد نظر خودت رو انتخاب کنی
        'outtmpl': 'downloads/%(id)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=True)
        video_file = ydl.prepare_filename(info_dict)
    app.send_document(message.chat.id, video_file)

app.run()

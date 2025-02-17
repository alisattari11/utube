import os
import yt_dlp
from pyrogram import Client, filters

# اطلاعات ربات (توکن را از BotFather بگیرید)
API_ID = 123456  # از my.telegram.org بگیرید
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"

app = Client("yt_downloader_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# انتخاب کیفیت از بین گزینه‌های موجود
def get_best_format(url, quality):
    ydl_opts = {
        'format': f'bestvideo[height<={quality}]+bestaudio/best',
        'outtmpl': 'downloaded_video.%(ext)s'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)

# فرمان دریافت لینک و دانلود ویدیو
@app.on_message(filters.command(["start", "help"]))
def send_welcome(client, message):
    message.reply_text("سلام! لینک یوتیوب رو بفرستید و کیفیت رو مشخص کنید (مثلاً 720 یا 1080).")

@app.on_message(filters.text)
def download_video(client, message):
    try:
        url, quality = message.text.split()  # لینک + کیفیت مثل "https://youtube.com/... 720"
        quality = int(quality)
        
        msg = message.reply_text("در حال دانلود ویدیو...")
        video_path = get_best_format(url, quality)

        msg.edit("ارسال ویدیو به تلگرام...")
        client.send_video(message.chat.id, video_path)

        os.remove(video_path)  # حذف فایل بعد از ارسال
    except Exception as e:
        message.reply_text(f"خطایی رخ داد:\n{str(e)}")

app.run()

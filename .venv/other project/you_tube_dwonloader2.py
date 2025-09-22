from pytube import YouTube

try:
    url = input("لطفاً لینک ویدیو یوتیوب را وارد کنید: ").strip()
    
    yt = YouTube(url)
    
    print(f"عنوان ویدیو: {yt.title}")
    print(f"تعداد بازدیدها: {yt.views:,}")
    
    stream = yt.streams.get_highest_resolution()
    
    print("در حال دانلود...")
    stream.download()
    
    print("دانلود با موفقیت انجام شد.")
    
except Exception as e:
    print("خطایی رخ داد:", str(e))
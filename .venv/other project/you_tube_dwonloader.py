from pytube import YouTube

try :
    url = input("Enter The url")
    
    yt=YouTube(url)
    
    print("Title:", yt.title)
    print("viwes:", yt.views)
    
    yd = yt.streams.get_highest_resolution()
    
    yd.download()
    print("Download is Starting")
    
except Exception as e:
    print("Error uncurred:", str(e))
    
from pytube import YouTube
link = input("Enter Youtube Link : ")
print("Downloading . . .")
yt = YouTube(link)
yd = yt.streams.get_highest_resolution().download(output_path='.')
print("Video Downloaded Successfully")


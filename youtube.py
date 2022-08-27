from pytube import YouTube
link = input("Enter your url\n")
yt = YouTube(link)
videos = yt.streams.all()
video = list(enumerate(videos))
for i in video :
    print(i)

print("Enter the desired option to download the format\n")
dn_option = int(input("enter the option\n"))
dn_video = videos[dn_option]

dn_video.download()
print("Successfully download")
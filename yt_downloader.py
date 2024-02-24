from pytube import YouTube
import time
import sys
import os

def download_url(video_url, output_path='./'):
    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.get_highest_resolution()

        print(f"Downloading: {yt.title}")
        print(f"Resolution: {video_stream.resolution}")

        video_stream.download(output_path)
        print("Download completed!")

    except Exception as e:
        print(f"Error: {str(e)}")

def download_file(filename, output_path='./'):
    try:
        with open(filename) as file:
            a = []
            for line in file:
                line = line.strip()
                yt = YouTube(line)
                title = yt.title
                res = line.split("index=", 1)
                num = res[1]
                addZeros = 3 - len(res[1])
                for i in range(addZeros):
                    num = "0" + num

                video_stream = yt.streams.get_highest_resolution()
                video_stream.download(output_path)
                print("Downloaded", yt.title)
                time.sleep(10)
                try:
                    os.rename(yt.title + ".mp4", num + "_" + yt.title + ".mp4")
                    print("Renamed", yt.title)
                except Exception as e:
                    a.append(num + "_" + yt.title)
        for line in a:
            print(line)

    except Exception as e:
        print(f"Error: {str(e)}")

print("\nENTER THE FOLLOWING NUMBER:\n   --[1]: input url\n   --[2]: input text file\n")
download_type = int(input())

if download_type == 1:
    video_url = input("Input url: ")
    download_url(video_url)
elif download_type == 2:
    filename = input("Filename: ")
    download_file(filename)

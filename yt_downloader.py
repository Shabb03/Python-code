#!/usr/bin/env python3

from pytube import YouTube

link = input("Enter link:")
yt = YouTube(link)

print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length, "seconds")

ys = yt.streams.filter(file_extension='mp4').get_by_itag(22)
ys.download()
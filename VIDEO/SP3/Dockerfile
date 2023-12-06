FROM ubuntu:20.04

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY bbb_7s.mp4 /app/bbb_7s.mp4

COPY background.jpg /app/background.jpg

RUN ffmpeg -i bbb_7s.mp4 -vf scale=640:480 bbb_7s_lowres.mp4

RUN ffmpeg -i background.jpg -vf format=gray,scale=1920:-1 -q:v 51 bg_compressed.jpg

# docker cp scavsp3:/app/bbb_7s_lowres.mp4 home/alvie/Escritorio/SCAV/VIDEO/SP3


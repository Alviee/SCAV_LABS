GUI COMMENTS:

I used PyQt5 for building from scratch my GUI and I used some functions of the previous labs. In the folder there is attached the gifs and images used and some .mp4 and .jpg for choosing the videos and performing the FFMPEG Tasks. There is also incorporated music in the GUI and some other easter eggs!! :P. I also implemented some pop up messages to let the user know when the actions of choosing video or photo are performed successfully or not. In the backend, it only lets the user take an .mp4 or .webm video, and for the images it lets only choose .jpg, .jpeg and .png, but that can be modified.

I did not manage to make the GUI interact with the user when the user wants to do the same operation twice, since in the Python terminal it pops up the overwrite file message.

Finally, as for the dimensions of the GUI, I tried to resize every event on it so that it can be scallable at fullscreen or depending on the device it does not change the dimensions. Although it does not stay at the middle and everything moves as a pack, it stays consistent.


DOCKER INSTRUCTIONS:

I left an image and a video so that in the Dockerfile it performs an ffmpeg operation and it provides a black & white lowered resolution image and a lowered resolution 7 seconds of Big Buck Bunny. Then, when the Dockerfile is run in a container, the files are created in it and what I had to do to obtain them locally is the following steps:

1. Build the image [sudo docker build -t scavsp3 .] in the folder the Dockerfile is located.

2. Run the image [sudo docker run -it --rm scavsp3] in the same folder.

3. For checking the files generated I used [ll] and there should be 4 files.

4. In another terminal, run [sudo docker ps] to obtain the container ID

5. For every file run [sudo docker cp container_id:/app/file.ext /path/to/local/folder] in my case:
sudo docker cp 1047a727af50:/app/bbb_7s_lowres.mp4 home/alvie/Escritorio/SCAV/VIDEO/SP3
sudo docker cp 1047a727af50:/app/bg_compressed.jpg home/alvie/Escritorio/SCAV/VIDEO/SP3

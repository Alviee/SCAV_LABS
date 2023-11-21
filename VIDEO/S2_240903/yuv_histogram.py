import os
import subprocess
import main_p3 as mp_3


# Exercise 6
def yuv_video_hist(filename, w, h):
    output_file = str(input('Name of the output file mp4 with the YUV histogram added (with extension): '))
    command = ('ffmpeg -i ' + filename + ' -filter_complex "split=2[a][b];[b]format=yuv420p,' +
                                         'histogram,format=yuva444p,scale=' + w + ':' + h + '[hh];' +
                                         '[a][hh]overlay" ' + output_file)
    os.system(command)
    return output_file


def size_video(filename):
    command = ('ffprobe -v error -show_entries stream=width,height ' + filename)
    output = subprocess.check_output(command, shell=True)
    lines = output.decode('utf-8').splitlines()
    width = lines[1].split('=')[1]
    height = lines[2].split('=')[1]
    return width, height


if __name__ == '__main__':
    # Init the filename
    init_filename = 'bunny.mp4'
    w_file, h_file = size_video(init_filename)

    bbb_p3_ops = mp_3.BBB_OPERATIONS()
    bbb_shortened = bbb_p3_ops.cut_video(init_filename)

    bbb_yuv_hist = yuv_video_hist(bbb_shortened, w_file, h_file)


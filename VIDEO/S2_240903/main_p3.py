import os
import subprocess
import yuv_histogram as yuv_hist
import subtitle_script as sub_p3


class BBB_OPERATIONS():

    def __init__(self):
        pass

    def cut_video(self, filename):
        start_time = str(input('Select a start time (hh:mm:ss): '))
        duration = str(input('Select a duration time (hh:mm:ss): '))
        output_file = str(input('Name of the mp4 file cut in time (with extension): '))
        command = ('ffmpeg -ss ' + start_time + ' -i ' + filename +
                   ' -t ' + duration + ' -c copy ' + output_file)
        os.system(command)
        return output_file

    def display_macro_motion(self, filename):
        output_file = str(input('Name of the output file with motion vectors (with extension): '))
        macroblock_command = ('ffmpeg -flags2 +export_mvs -i ' + filename +
                              ' -vf codecview=mv=pf+bf+bb ' + output_file)
        os.system(macroblock_command)

    def bbb_container(self, filename):
        shorten_vid = self.cut_video(filename)
        output_vid1 = str(input('Name of the output file mp3 mono (with extension): '))
        command1 = ('ffmpeg -i ' + shorten_vid + ' -ac 1 ' + output_vid1)
        output_vid2 = str(input('Name of the output file mp3 stereo with lower bitrate (with extension): '))
        quality_factor = int(input('Select a quality factor from 0 (best quality) to 9 (worst quality)'))
        command2 = ('ffmpeg -i ' + shorten_vid + ' -q:a ' + str(quality_factor) + ' ' +
                    output_vid2)
        output_vid3 = str(input('Name of the output file aac (with extension): '))
        command3 = ('ffmpeg -i ' + shorten_vid + ' -c:a aac ' + output_vid3)

        output_vid4 = str(input('Name of the output file mp4 with all previous outputs packed (with extension): '))
        command4 = ('ffmpeg -i ' + shorten_vid + ' -i ' + output_vid1 + ' -i ' +
                    output_vid2 + ' -i ' + output_vid3 + ' -map 0:v -map 1:a -map 2:a -map 3:a ' + output_vid4)
        os.system(command1)
        os.system(command2)
        os.system(command3)
        os.system(command4)
        return output_vid1, output_vid2, output_vid3, output_vid4

    def container_reader(self, filename):
        command = ('ffmpeg -i ' + filename + ' 2>&1 | grep Stream | wc -l')
        output = subprocess.check_output(command, shell=True)
        number_output = str(output.decode('utf-8').strip())
        print('The number of tracks the container contains is: ' + number_output)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Init the filename
    init_filename = 'bunny.mp4'
    init_subtitles = 'Lights_in_the_dusk_2006_FINNISH.srt'

    # Exercise 1
    var = BBB_OPERATIONS()
    print("For this exercise, you will create a video that shows the motion vectors. " +
          "For doing it, cut the initial video into a 9 seconds video and name the motion vector video.")

    bbb_shorten = var.cut_video(init_filename)

    var.display_macro_motion(bbb_shorten)

    # Exercise 2
    print("For this exercise, you will have to cut a 50 second video and obtain its mono .mp3 audio, the stereo " +
          ".mp3 audio with lower bitrate (asked after the name), the .aac audio and the resulting packed .mp4 video.")
    mp3_mono, mp3_stereo_low_br, aac_audio, mp4_packed = var.bbb_container(init_filename)

    # Exercise 3
    print("For this exercise, you will obtain the number of tracks an .mp4 container contains.")
    var.container_reader(mp4_packed)

    # Exercise 5
    print("For this exercise, you will obtain an .mp4 video with downloaded subtitles (you will have to download " +
          "them). This exercise is inherited from subtitle_script.py script")
    bbb_5min_subtitles = var.cut_video(init_filename)
    bbb_subtitled = sub_p3.subtitled_video(bbb_5min_subtitles, init_subtitles)

    # Exercise 6
    print("For this exercise, you will obtain an .mp4 video with the YUV histogram " +
          "them). This exercise is inherited from yuv_histogram.py script")
    bbb_weight, bbb_height = yuv_hist.size_video(init_filename)
    bbb_yuv_hist = yuv_hist.yuv_video_hist(bbb_5min_subtitles, bbb_weight, bbb_height)
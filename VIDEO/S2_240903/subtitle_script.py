import os
import main_p3 as mp_3


# Exercise 4
def subtitled_video(filename, subtitles):
    output_file = str(input('Name of the output file mp4 with the subtitles added (with extension): '))
    command = ('ffmpeg -i ' + filename + ' -vf "subtitles=' + subtitles + '" ' +
               output_file)
    os.system(command)
    return output_file


if __name__ == '__main__':
    # Init the filename
    init_filename = 'bunny.mp4'
    init_subtitles = 'Lights_in_the_dusk_2006_FINNISH.srt'

    bbb_p3_ops = mp_3.BBB_OPERATIONS()
    bbb_shortened = bbb_p3_ops.cut_video(init_filename)

    bbb_subtitled = subtitled_video(bbb_shortened, init_subtitles)
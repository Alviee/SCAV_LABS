# ÁLVARO JIMENEZ | NIA: 240903
import os

class GUI_FUNCTIONS():
    def __init__(self):
        pass

    def display_macro_motion_GUI(self, filename):
        file_ext = filename.split('.')
        output_file = 'macro_video_GUI.' + file_ext[1]
        macroblock_command = ('ffmpeg -flags2 +export_mvs -i ' + filename +
                              ' -vf codecview=mv=pf+bf+bb ' + output_file)
        os.system(macroblock_command)

    def lower_resolution_GUI(self, filename):
        file_ext = filename.split('.')
        resolution_input = 144
        video_height = str(int(resolution_input))
        video_width = str(int((resolution_input / 9) * 16))
        output_vid = 'lower_resolution.' + file_ext[1]
        command = ('ffmpeg -i ' + filename + ' -vf scale=' + video_width + 'x' + video_height + ',setsar=1:1 '
                   + output_vid)
        os.system(command)
        return output_vid

#if __name__ == '__main__':


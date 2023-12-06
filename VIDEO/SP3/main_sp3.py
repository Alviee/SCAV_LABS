# ÁLVARO JIMENEZ | NIA: 240903
import os
import time
import P2.code.main_p2 as m_p2

class BBB_SP3():
    def __init__(self):
        pass

    def video_converter(self, filename):
        var_bool = int(input("Select resolution option: 0 for a resolution number (720p, 480p); 1 for " +
                             "indicating these resolutions [360x240] or [160x120]: "))
        while var_bool != 0 and var_bool != 1:
            var_bool = int(input("Wrong selection. Select resolution option: 0 for a resolution number " +
                                 "(720p, 480p); 1 for indicating these resolutions [360x240] or [160x120]: "))
        if var_bool == 0:
            print("Option 0 selected. You should select 720 or 480 in the resolution input to follow the exercise. " +
                  "Aspect ratio for 720 should be 16:9. Aspect ratio for 480 should be 4:3.")
            res_video = m_p2.resolution_manager(filename)
            return res_video
        else:
            print("Option 1 selected. You should select '360x240' or '160x120' in the following resolution inputs " +
                  "The aspect ratio is already computed: ")
            res_var = str(input("Write the resolution of the code: '360x240' or '160x120' only options allowed: "))
            while res_var != '360x240' and res_var != '160x120':
                res_var = str(input("Wrong input. Write the resolution of the code: '360x240' or '160x120' " +
                                    "only options allowed: "))
            res_list = res_var.split('x')
            output_vid = ('im_res_' + res_list[0] + "_" + res_list[1] + ".mp4")
            command = ('ffmpeg -i ' + filename + ' -vf scale=' + res_list[0] + 'x' + res_list[1] + ',setsar=1:1 '
                       + output_vid)
            os.system(command)
            return output_vid

    def change_video_encoder(self, filename):
        res_video = self.video_converter(filename)
        time.sleep(2)
        output_video = str(input('Write the name of the output video WITHOUT the extension (e.g. bbb_vp8): '))
        encoding_list = ['VP8', 'VP9', 'h265', 'AV1']
        encoder = str(input("Select an encoder [VP8, VP9, h265, AV1 (this might not compile)] "))
        while encoder not in encoding_list:
            encoder = str(input('Wrong input. Select an encoder [VP8, VP9, h265, AV1]: '))
        if encoder == encoding_list[0]:
            command = ("ffmpeg -i " + res_video + " -c:v libvpx -b:v 1M -c:a libvorbis " + output_video + '.webm')
            os.system(command)
            return output_video + '.webm', encoder
        elif encoder == encoding_list[1]:
            command = ("ffmpeg -i " + res_video + " -c:v libvpx-vp9 -b:v 1M -c:a libvorbis " + output_video + '.webm')
            os.system(command)
            return output_video + '.webm', encoder

        elif encoder == encoding_list[2]:
            command = ("ffmpeg -i " + res_video + " -c:v libx265 -crf 10 " + output_video + '.mp4')
            os.system(command)
            return output_video + '.mp4', encoder

        elif encoder == encoding_list[3]:
            command = ("ffmpeg -i " + res_video + " -c:v libaom-av1 -crf 10 " + output_video + '.mp4')
            os.system(command)
            return output_video + '.mp4', encoder

    def encoder_comparator(self, filename):
        first_encoder_video, first_encoder = self.change_video_encoder(filename)
        time.sleep(3)
        second_encoder_video, second_encoder = self.change_video_encoder(filename)
        time.sleep(3)
        output_video = str(input("Write the mp4 output video name with the extension: "))
        command = ('ffmpeg -i ' + first_encoder_video + ' -i ' + second_encoder_video + ' -filter_complex ' +
                   '"[0:v]pad=iw*2:ih[int];[int][1:v]overlay=W/2:0[vid]" -map "[vid]" ' + output_video)
        os.system(command)
        return output_video, first_encoder, second_encoder


if __name__ == '__main__':
    # Load images
    big_buck_bunny = 'bbb_7s.mp4'

    p3_class = BBB_SP3()
    # Exercise 1
    quality_video = p3_class.change_video_encoder(big_buck_bunny)
    # Exercise 2
    comparison_video, encoder1, encoder2 = p3_class.encoder_comparator(big_buck_bunny)

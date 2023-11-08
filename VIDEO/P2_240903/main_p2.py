import os
import P1.main_p1 as p1


# Exercise 1
def mp4_to_mpeg(filename):
    command = 'ffmpeg -i ' + filename + ' big_buck_bunny.mpeg'
    command2 = ('ffprobe -v quiet -show_streams -show_format ' + filename +
                '> big_buck_bunny_output.txt')
    os.system(command)
    os.system(command2)


# Exercise 2
def resolution_manager(filename):
    '''
    I made this exercise interactively, so that the user can introduce the resolution desired and the aspect ratio.
    With this, the user not only will be able to obtain a video with more or less quality, but larger or smaller file
    sizes and at the same time videos to different devices (e.g. 9:16 for mobile devices).
    '''
    resolution_list = [144, 240, 360, 480, 720, 1080]
    aspect_ratio = ['1:1', '4:3', '16:9']
    resolution_input = float(input("Choose your resolution (144, 240, 360, 480, 720 or 1080): "))
    aspect_input = str(input("Choose your aspect ratio (1:1, 4:3, 16:9): "))

    while resolution_input not in resolution_list or aspect_input not in aspect_ratio:
        if resolution_input not in resolution_list:
            resolution_input = float(input("Incorrect value. Choose your resolution (144, 240, 360, 480, 720 or 1080)"
                                           + ": "))
        else:
            aspect_input = str(input("Incorrect value. Choose your aspect ratio (1:1, 4:3, 16:9): "))

    aspect_ratio_list = [int(i) for i in aspect_input.split(':')]
    video_height = str(int(resolution_input))
    video_width = str(int((resolution_input / aspect_ratio_list[1]) * aspect_ratio_list[0]))
    command = ('ffmpeg -i ' + filename + ' -vf scale=' + video_width + 'x' + video_height + ',setsar=1:1 '
               + 'im_res_' + str(aspect_ratio_list[0]) + ":" + str(aspect_ratio_list[1]) + '_' + video_width + 'x' +
               video_height + '.mp4')
    os.system(command)


# Exercise 3
def chroma_subsampling_changer(filename):
    '''
    Concretely, with our video, we will not perceive any changes, since the subsampling cannot be performed
    to a higher sampling and the video is already sampled at 4:2:0. Then, we will not be able to subsampling it
    more.
    '''
    chroma_sub_list = ['4:2:0', '4:1:1', '4:2:2', '4:4:4']
    chroma_sub_input = str(input("Choose your chroma subsampling ratio (4:2:0, 4:1:1, 4:2:2, 4:4:4): "))
    while chroma_sub_input not in chroma_sub_list:
        chroma_sub_input = str(input("Incorrect input. Choose your chroma subsampling ratio " +
                                     "(4:2:0, 4:1:1, 4:2:2, 4:4:4): "))
    chroma_sub_output = [i for i in chroma_sub_input.split(':')]
    yuv_value = 'yuv' + chroma_sub_output[0] + chroma_sub_output[1] + chroma_sub_output[2] + 'p'
    command = ('ffmpeg -i ' + filename + ' -c:v libx264 -vf format=' + yuv_value +
               ' im_subsampled_' + yuv_value + '.mp4')
    os.system(command)


# Exercise 4
def video_info(filename):
    command = ('ffprobe -v quiet -show_streams -show_format ' + filename)
    os.system(command)


if __name__ == '__main__':
    # Load images
    big_buck_bunny = 'big_buck_bunny.mp4'
    bellossom = "bellossom.png"

    # Exercise 1
    mp4_to_mpeg(big_buck_bunny)

    # Exercise 2
    resolution_manager(big_buck_bunny)

    # Exercise 3
    chroma_subsampling_changer(big_buck_bunny)

    # Exercise 4
    video_info(big_buck_bunny)

    # Exercise 5 (inherited in the beginning of the code). Use some functions from P1
    # Get width and height
    bellossom_w, bellossom_h = p1.get_imsize(bellossom)

    # (P1) Exercise 2
    p1.lower_quality_image(bellossom)

    # (P1) Exercise 3
    p1.serpentine(bellossom)

    # (P1) Exercise 4
    p1.bw_compression(bellossom)





import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import os
from natsort import natsorted, ns
from skimage import data, io
import crop


if __name__ == '__main__':
    input_directory = '/Users/vincentsheehan/Drawing/Drawings Archive/Sketchpads/~1999-'    # Modify/make user
                                                                                            # selectable for Github.
    output_directory = input_directory + '_modified'

    # List files in input directory and sort by name.
    file_list = os.listdir(input_directory)
    file_list = natsorted(file_list)
    file_list.pop()    # Remove last element (folder icon reference, if folder icon modified).
    print(file_list)

    # Create list of numpy arrays from image files.
    image_list = []
    for filename in file_list:
        image_list.append(io.imread(input_directory + "/" + filename))

    # Perform crop on all elements in list.
    crop.crop_all(image_list)

    # Display image - For crop size estimation. To be removed.
    fig = plt.figure()
    gs = GridSpec(1, 2)

    ax0 = fig.add_subplot(gs[0, 0])
    ax1 = fig.add_subplot(gs[0, 1])

    ax0.imshow(image_list[0])
    ax1.imshow(image_list[20])

    plt.show()

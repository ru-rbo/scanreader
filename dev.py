from pathlib import Path

import matplotlib.pyplot as plt

import scanreader as sr


def quick_save_image(arr, save_path):
    fig, ax = plt.subplots()
    ax.imshow(arr[:, :, 5, 300])
    plt.savefig(save_path)


# set up directories
datapath = Path('/data2/fpo/data/high_res')
save_directory = Path('/data2/fpo/data/') / 'temp'
save_directory.mkdir(exist_ok=True, parents=True)
save_name = 'example_image.png'
full_savepath = save_directory / save_name

# read in the data
file = [str(x) for x in datapath.glob("*.tif*")][0]  # grab the first file in the directory
scan = sr.read_scan(file, join_contiguous=True, lbm=True, x_cut=(6, 6), y_cut=(30, 1))
data = scan[0]

# save an example image
quick_save_image(data, full_savepath)

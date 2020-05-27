import nibabel as nib
from PIL import Image
import numpy as np
import argparse


def colour(input_path, output_path):
    im = nib.load(input_path)
    data = np.asanyarray(im.get_fdata(), dtype='int8', order='F')
    z_shape = int(data.shape[2]/2)

    data -= 127
    data = data[:, :, z_shape]
    rgb_data = np.stack((data,)*3, axis=-1)

    mappings = { el: list(np.random.choice(range(256), size=3)) for el in np.unique(data)}

    for x in range(rgb_data.shape[0]):
        for y in range(rgb_data.shape[1]):
            rgb_data[x,y] = mappings[data[x, y]]

    
    new_im = Image.fromarray(rgb_data, 'RGB').save(output_path)

def main():

    parser = argparse.ArgumentParser(description='Create a coloured image slice from an anatomical NIfTI image')
    parser.add_argument('input_path', type=str,
                        help='input NIfTI image')
    parser.add_argument('output_path', type=str,
                        help='output filepath. should be a Pillow accepted image format')

    args = parser.parse_args()
    

#colour("/home/valeriehayot/Documents/code/passthrough/source/ds000206-download/sub-THP0001/ses-THP0001CCF1/anat/sub-THP0001_ses-THP0001CCF1_run-01_T1w.nii.gz", "colouredbrain.png")

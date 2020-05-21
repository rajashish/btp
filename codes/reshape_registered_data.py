import os
import numpy as np
import nibabel as nib
from scipy.ndimage import zoom

atls = nib.load('registered_hc/sub001.nii.gz')
print(atls.shape)
data = atls.get_fdata()
data1 = data[19:128,10:128,19:128]
hdr = atls.header
f_data = data1[:91,:109,:91]
# print(new_array.shape)

img = nib.Nifti1Image(f_data, np.eye(4))
# nib.save(img, os.path.join('/','final_atlas.nii.gz'))
img.to_filename('registered_hc_2mm/sub001r.nii.gz')

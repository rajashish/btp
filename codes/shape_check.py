import os
import numpy as np
import nibabel as nib


atls = nib.load('mni/MNI152lin_T1_2mm_brain.nii.gz')
print(atls.shape)

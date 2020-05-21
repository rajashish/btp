import os
import numpy
import nibabel as nib
#atls = nib.load('final_atlas.nii.gz')
atls = nib.load('des-killVolumetric2mm.nii.gz')

data = atls.get_fdata()
i=0
j=0
k=0
for i in range(0,61):
	for j in range(0,73):
		for k in range(0,61):
			if (data[i][j][k] != 0.0):
				print(data[i][j][k])
				

	
print(data[0][22][8])
import os
import numpy as np
import nibabel as nib
import statistics
import json
import pandas
from label_list import *
#atls = nib.load('final_atlas.nii.gz')
atls = nib.load('final_atlas.nii.gz')
dat = nib.load('registered_ca/sub046.nii.gz')
dat1 = dat.get_fdata()
x,y,z,t = dat.shape
print("t : " , dat.shape)
label = [1001,1002,1003,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,8,10,11,12,13,17,18,26,28,2001,2002,2003,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,47,49,50,51,52,53,54,58,60]

data = atls.get_fdata()
atlas = []
final_data = []
for i in range(86):
	final_data.append([])
for c in range(t):
	print("c :", c )
	f_data = []

	for i in range(86):
		f_data.append([])

	# for i in range(91):
	# 	for j in range(109):
	# 		for k in range(91):
	# 			if(dat1[i][j][k][c]!=0.0):
	# 				for m in range(86):
	# 					if(data[i][j][k]==label[m]):
	# 						f_data[m].append(dat1[i][j][k][c])
	# 						break

	for i in range(86):
		for j in range(len(list1[i])):
			x = list1[i][j]
			y = list2[i][j]
			z = list3[i][j]
			if(dat1[x][y][z][c]!=0.0):
				f_data[i].append(dat1[x][y][z][c])
	for i in range(86):
		if(len(f_data[i])!=0):
			final_data[i].append(statistics.mean(f_data[i]))
		else:
			final_data[i].append(0.0)


## FUNCTIONAL CONNECTIVITY AND CORRELATION



da = pandas.DataFrame(final_data)
s = da.transpose()
ss = s.corr(method = 'pearson')
ss.fillna(0, inplace = True)
print(ss)
# p = ss.values.tolist()
ss.to_excel(r'~/btp/ca_fc/fc046.xlsx',index = False,header = False)
# with open('hc_fc/fc_001.txt','w') as fl:
# 	json.dump(final_data,fl)

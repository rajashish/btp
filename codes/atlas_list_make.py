import os
import numpy
import nibabel as nib
import statistics
#atls = nib.load('final_atlas.nii.gz')
atls = nib.load('final_atlas.nii.gz')
label = [1001,1002,1003,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,8,10,11,12,13,17,18,26,28,2001,2002,2003,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,47,49,50,51,52,53,54,58,60]
list1 = []
list2 = []
list3 = []
data1 = atls.get_fdata()
for i in range(86):
	list1.append([])
	list2.append([])
	list3.append([])
for i in range(91):
	for j in range(109):
		for k in range(91):
			for cc in range(86):
				if(data1[i][j][k]==label[cc]):
					list1[cc].append(i)
					list2[cc].append(j)
					list3[cc].append(k)
print("list1 = " ,list1,"\n\n\n\n\n")
print("list2 = ",list2,"\n\n\n\n\n")
print("list3 = " ,list3,)



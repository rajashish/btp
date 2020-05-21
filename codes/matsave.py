import pandas as pd
import scipy.io as sio
import numpy 
import random


# file1 = '../hc_fc/fc005.xlsx'
# file2 = '../hc_fc/fc007.xlsx'

# file1 = ('../hc_sc/0005_fdt_network_matrix.xlsx')
# file2 = ('../hc_sc/0007_fdt_network_matrix.xlsx')
hc = ['005','007','021','029','031','033','036','038','042','044','049','050','051','054','055','062']
ca = ['008','009','013','015','016','017','018','019','020','023','024','026','027','030','034','035','040','043','045','046']

# x1 = pd.ExcelFile(file1)
# x2 = pd.ExcelFile(file2)
# data1 = x1.parse('Sheet1',header = None)
# dat1 = data1.values.tolist()
# data2 = x2.parse('Sheet1',header = None)
# dat2 = data2.values.tolist()
# f_data1 = []
# f_data1.append(dat1)
# f_data1.append(dat2)
# g = numpy.array(f_data1)
# g1 = numpy.transpose(g)
# f_data = g1.tolist()
# f_data1 = []
# for i in range(len(ca)):
# 	fl = '../ca_fc/fc' + ca[i] + '.xlsx'
# 	# fl = '../ca_sc/0' + ca[i] + '_fdt_network_matrix.xlsx'
# 	x =  pd.ExcelFile(fl)
# 	data1 = x.parse('Sheet1',header = None)
# 	dat1 = data1.values.tolist()
# 	f_data1.append(dat1)

# for i in range(len(hc)):
# 	fl = '../hc_fc/fc' + hc[i] + '.xlsx'
# 	# fl = '../hc_sc/0' + hc[i] + '_fdt_network_matrix.xlsx'
# 	x =  pd.ExcelFile(fl)
# 	data1 = x.parse('Sheet1',header = None)
# 	dat1 = data1.values.tolist()
# 	f_data1.append(dat1)
# g = numpy.array(f_data1)
# g1 = numpy.transpose(g)
# f_data = g1.tolist()
# print(len(f_data[0][0]))




f_data1 = []
# for p in range(46):
# 	i = random.randint(0,19)
# 	# fl = '../ca_fc/fc' + ca[i] + '.xlsx'
# 	fl = '../ca_sc/0' + ca[i] + '_fdt_network_matrix.xlsx'
# 	x =  pd.ExcelFile(fl)
# 	data1 = x.parse('Sheet1',header = None)
# 	dat1 = data1.values.tolist()
# 	f_data1.append(dat1)
for p in range(46):
	i = random.randint(0,15)
	# fl = '../hc_fc/fc' + hc[i] + '.xlsx'
	fl = '../hc_sc/0' + hc[i] + '_fdt_network_matrix.xlsx'
	x =  pd.ExcelFile(fl)
	data1 = x.parse('Sheet1',header = None)
	dat1 = data1.values.tolist()
	f_data1.append(dat1)
g = numpy.array(f_data1)
g1 = numpy.transpose(g)
f_data = g1.tolist()
print(len(f_data[0][0]))

#print(data1)
sio.savemat('../hc_sc_bootstrap2.mat',{'data':f_data})

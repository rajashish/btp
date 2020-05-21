import scipy.io
import numpy as np
import matplotlib.pyplot as plt
mat = scipy.io.loadmat('../MKL-master/hc_MKL_bootstrap2.mat')
mat1 = scipy.io.loadmat('../MKL-master/ca_MKL_bootstrap2.mat')
s = mat['MKL']['pi'][0][0]
s1 = mat1['MKL']['pi'][0][0]

i=0
for n in range(16):

	H = np.array(s[i:i+86][:])
	H1 = np.array(s1[i:i+86][:])
	print(H1.shape)
	fig = plt.figure(figsize=(6,3.2))
	ax = fig.add_subplot(122)
	sr = 'HC_' + 'kernel'+str(n+1)
	ax.set_title(sr)
	plt.imshow(H)
	plt.colorbar()
	ax = fig.add_subplot(121)
	sr = 'CA_' + 'kernel'+str(n+1)
	ax.set_title(sr)
	plt.imshow(H1)
	plt.colorbar()
	ax.set_aspect('equal')
	plt.savefig('../plots/bootstrap/2/fig_' + str(n))
	# plt.show()
	i+=86
	
	print(len(s))
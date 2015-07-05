# -*- coding:utf-8 -*-
import sys
import numpy as np
import matplotlib.pyplot as plt
import smooth


def smoothTouchLog(inputPath):
	# 1. load file
	data = np.genfromtxt(inputPath, dtype=None, delimiter=',', names=True) 
	print data
	tdata = data["timestamp"]
	adata = data["action"]
	xdata = data["x"]
	ydata = data["y"]
	
	# 2. filter data
	for i in range(0, len(adata)):
		index = len(adata) -i-1
		if adata[index] == "ACTION_UP" or xdata[index] < 0 or ydata[index] < 0:
			tdata = np.delete(tdata, index)
			xdata = np.delete(xdata, index)
			ydata = np.delete(ydata, index)

	# 3. time normalize
	tdata2 = (tdata - tdata[0])
	
	# 4. interpolation
	tdata_output = range(np.amin(tdata2), np.amax(tdata2), 1)
	xdata_output = np.interp(tdata_output, tdata2, xdata)
	ydata_output = np.interp(tdata_output, tdata2, ydata)
	
	# 5. graph
	plt.plot(xdata, ydata, label='Original Data')
	plt.plot(xdata_output, ydata_output, label='Interpolation Data')
	plt.legend()
	plt.show()


if __name__ == "__main__":
	inputPath = r"touchdata.csv"
	smoothTouchLog(inputPath)

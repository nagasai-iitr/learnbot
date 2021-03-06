from __future__ import print_function, absolute_import
import numpy as np, sys, os

path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(path)
import visual_auxiliary as va

def is_center_black_line(lbot):
	frame = lbot.getImage()
	rois = va.detect_black_line(frame)
	maxIndex = np.argmax(rois)
	if maxIndex==1 and rois[maxIndex]>20:
		return True
	return False

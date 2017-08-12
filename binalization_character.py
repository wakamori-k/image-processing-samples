#coding:utf-8
import numpy as np
import cv2
import matplotlib.pyplot as plt

def binalization(org_img):
	gry_img = cv2.cvtColor(org_img, cv2.COLOR_BGR2GRAY)

	# Calc threshold 
	T, bin_img = cv2.threshold(gry_img, 127, 255, cv2.THRESH_BINARY) 

	return bin_img

def adaptive_binalization(org_img):
	gry_img = cv2.cvtColor(org_img, cv2.COLOR_BGR2GRAY)

	# Calc threshold 
	#bin_img = cv2.adaptiveThreshold(gry_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5)
	bin_img = cv2.adaptiveThreshold(gry_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 5)

	return bin_img

def binalization_otsu(org_img):
	gry_img = cv2.cvtColor(org_img, cv2.COLOR_BGR2GRAY)

	# Calc threshold on gram_img using OTSU THRESHOLD
	T, bin_img = cv2.threshold(gry_img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) 

	return bin_img

def binalization_otsu_after_gaussian_filtering(org_img):
	gry_img = cv2.cvtColor(org_img, cv2.COLOR_BGR2GRAY)

	# Calc threshold 
	gray_gf = cv2.GaussianBlur(gry_img, (3,3), 0)
	T, bin_img = cv2.threshold(gray_gf, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

	return bin_img

def main():
	#img_path = "figure/english_letter.jpg"
	img_path = "figure/enter_graduate.jpg"
	img = cv2.imread(img_path, cv2.IMREAD_COLOR ) # COLOR MODE
	#img = cv2.imgread(img_path, cv2.IMREAD_GRAYSCALE ) # GRAY SCALE MODE

	img_list = []
	img_name_list = []

	height, width, channels = img.shape[:3]
	img = cv2.resize(img, (500, int(height*(500.0/width))))
	img_list.append(img)
	img_name_list.append("original")

	result_img = binalization(img)
	img_list.append(result_img)
	img_name_list.append("normal binalization")

	result_img = adaptive_binalization(img)
	img_list.append(result_img)
	img_name_list.append("adaptive binalization")

	result_img = binalization_otsu(img)
	img_list.append(result_img)
	img_name_list.append("otsu binalization")

	result_img = binalization_otsu_after_gaussian_filtering(img)
	img_list.append(result_img)
	img_name_list.append("otsu after gaussian filtering binalization")

	for i in xrange(len(img_list)):
		plt.subplot(round(len(img_list)/2.0), len(img_list)/2, i+1),plt.imshow(img_list[i],'gray')
	   	plt.title(img_name_list[i])
	   	plt.xticks([]),plt.yticks([])
	plt.show()


if __name__ == "__main__":
	main()
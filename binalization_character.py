#coding:utf-8
import numpy as np
import cv2

def binalization_otsu(org_img):
	gry_img = cv2.cvtColor(org_img, cv2.COLOR_BGR2GRAY)
	
	# Calc threshold on gram_img using OTSU THRESHOLD
	T, bin_img = cv2.threshold(gry_img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU) 

	return bin_img


def main():
	img_path = "figure/english_letter.jpg"
	img = cv2.imread(img_path, cv2.IMREAD_COLOR ) # COLOR MODE
	#img = cv2.imgread(img_path, cv2.IMREAD_GRAYSCALE ) # GRAY SCALE MODE

	cv2.imshow('original image', img)
	cv2.waitKey(0)

	result_img = binalization(img)

	cv2.imshow('result image', result_img)
	cv2.waitKey(0)

	cv2.destroyAllWindows()


if __name__ == "__main__":
	main()
from scipy.spatial import distance as dist
import numpy as np
import argparse
import cv2
import csv
import time


def histo(imagePath):
	image = cv2.imread(imagePath)
	# extract a 3D RGB color histogram from the image,
	# using 8 bins per channel, normalize, and update
	# the index
	hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8],
		[0, 256, 0, 256, 0, 256])
	hist = cv2.normalize(hist, hist).flatten()
	return hist

# construct the argument parser and parse the arguments


def processImages(args):
	output_file=  open(args["output"],'w')
	fieldnames = ['image1', 'image2', 'similar', 'elapsed']
	writer = csv.DictWriter(output_file, fieldnames=fieldnames)
	writer.writeheader()
	with open(args["input"]) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if line_count == 0:
				line_count += 1
				continue
			else:
				start_time = time.time()
				hist1=histo(row[0])
				hist2=histo(row[1])
				result=cv2.compareHist(hist1, hist2, cv2.HISTCMP_CHISQR)
				time_elapsed = time.time() - start_time
				writer.writerow({'image1': row[0], 'image2': row[1], 'similar': "%.2f"%(result), 'elapsed': "%.3f"%(time_elapsed)})
				line_count += 1
	output_file.close()

if __name__ == '__main__':
	ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required = True,
	help = "Input CSV file name")
ap.add_argument("-o", "--output", required = True,
	help = "Output CSV file name")
args = vars(ap.parse_args())
processImages(args)
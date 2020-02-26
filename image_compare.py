from scipy.spatial import distance as dist
import numpy as np
import argparse
import cv2
import csv
import time

#extract histogram
def histo(imagePath):
	image = cv2.imread(imagePath)
	# extract a 3D RGB color histogram from the image,
	# using 8 bins per channel and normalize
	hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8],
		[0, 256, 0, 256, 0, 256])
	hist = cv2.normalize(hist, hist).flatten()
	return hist

#Process images from input csv file and generate output csv file 
def processImages(args):
	#Open file handler for output file
	output_file=  open(args["output"],'w')
	#Declare field names for output csv file
	fieldnames = ['image1', 'image2', 'similar', 'elapsed']
	#Write header to output csv fiel
	writer = csv.DictWriter(output_file, fieldnames=fieldnames)
	writer.writeheader()
	#Open input csv file for processing
	with open(args["input"]) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			if line_count == 0:
				line_count += 1
				continue
			else:
				# Capture start time
				start_time = time.time()
				hist1=histo(row[0])
				hist2=histo(row[1])
				# compute the distance between the two histograms using the method HISTCMP_CHISQR
				result=cv2.compareHist(hist1, hist2, cv2.HISTCMP_CHISQR)
				# Calculate time elapsed in comparison
				time_elapsed = time.time() - start_time
				# Write results to output csv file
				writer.writerow({'image1': row[0], 'image2': row[1], 'similar': "%.2f"%(result), 'elapsed': "%.3f"%(time_elapsed)})
				# Increment line count
				line_count += 1
	# Close output file handler
	output_file.close()


# Start execution here
if __name__ == '__main__':

	# construct the argument parser and parse the arguments
	ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required = True,
	help = "Input CSV file name")
ap.add_argument("-o", "--output", required = True,
	help = "Output CSV file name")
args = vars(ap.parse_args())
processImages(args)
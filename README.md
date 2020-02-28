# image_compare
This script is used to find similarity between images. It is written in Pthon3.7 and uses OpenCV to compare color histogram of the images and generate score. It has used cv2.HISTCMP_CHISQR method which applies the Chi-Squared distance to the histograms.

# Setup

Install Pyhton 3 and then install virtualenv. Create a virtualenv with python 3. You can find the steps [here](https://docs.python-guide.org/dev/virtualenvs/)

Once virtualenv is setup, clone this repo and install the required Python packages using below command.

```pip3 install -r requirements.txt```

# Usage

This script takes two arguments `input csv file` and `output csv file`. You can mention the absoulte path of the files if it is not in the same location as that of the script. The input file must be in the csv format and contain files to be compared in below format. The image file should have absolute path.

```imag1,image2
SampleJPGImage_100kbmb.jpg,SampleJPGImage_100kbmb.png
example_image_comparison_unmodified.jpg,example_image_comparison_modified.jpg
```

Pull the latest code from master and run the command as foollows:

```python3 image_compare.py -i input.csv -o output.csv```

This will give output in the below format. Score format is limited to 2 decimal numbers whereas elapsed time is limited to 3 decimal numbers. These can modified in the scipt.

```image1,image2,similar,elapsed
SampleJPGImage_100kbmb.jpg,SampleJPGImage_100kbmb.png,0.00,0.026
example_image_comparison_unmodified.jpg,example_image_comparison_modified.jpg,0.01,0.032
```


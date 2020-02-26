# image_compare
This script is used to find similarity between images. It is written in Pthon3.7 and  used OpenCV to compare color histogram of the images and generate score.

# Setup

Install Pyhton 3 and then install virtualenv. Create a virtualenv with python 3. You can find the steps [here](https://docs.python-guide.org/dev/virtualenvs/)

Once virtualenv is setup, clone this repo and install the required Python packages using below command.

```pip3 install -r requirements.txt```

# Usage

This script takes two arguments `input csv file` and `output csv file`. You can mention the absoulte path of the files if it is not in the same location as that of the script.

```python3 image_compare.py -i input.csv -o output.csv```

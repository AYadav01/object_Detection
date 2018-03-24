# Haar Classifier for Image/Video Classification

**Version 1.0.0 ;-)**

Steps
---

* Collecting negative or background images

	Any image, that is not positive or the one that we want to detect, can be categorized as negative image. The more negative images we have, the better the classifer could be trained. The size of the images should be relatively small as it takes longer time to process large files.

* Preprocessing the images

	The images are converted to greyscale. The code also removes any blank or unsupported imags type.

* Creating positive images

	These images could be created manually; however, we decided to apply geometric transformation on one positive images then super impose it on all of our negative images. 

* Create a positive vector file by combining all the positive images

	The positive vector file provides the path to the positive images and the decsription file

* Train the Cascade


Description Files
---

The positive and negative images need description files.
* bg.txt: It contains the path to each image
* pos.txt: It contains the path to images, including, the number of objects and the location of the object in the image

Specification: 
---

* Image Library: 'http://image-net.org'
* Image analysis module: OpenCV
* Programming Language: Python
* Total images (Positive & Negative): 8000
* Images size: 50x50
* Server: Linux (Ubutu)


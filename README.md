# FABRIC STAIN DETECTION USING YOLOv3

## PROBLEM

### Fabric defect detection in textile production

Fabric defect detection is a part of fabric quality control in textile production. 
In textile companies, the detection of defects and unacceptable areas of fabrics at the quality control stage has great importance for apparel production, although it is also a post-manufacturing operation for weaving and knitting mills.

The fabric defects may cause 45-65% incurred loss in sale prices. Besides, approximately 85% of the product rejects in the apparel industry are related with fabric defects.

<br/>

### What fabric defects types are considered?

In industrial fabrics there are around  60 fabric defect types. Amongs these fabric defect types stain is the most abundant fabric defect. In this project fabric stain defects are considered. 

Fabric stains can be categorized into 3 types,
* Ink stains
* Dirt stains
* Oil stains

<img src="https://github.com/PrimeshShamilka/fabric_defect_detector/blob/master/images/Design/stain_types.png" width="400">
<br/>

### What fabric materials are considered?

Basically, fabric materials can be categorized into two categories as Textured material and Uniform material. Textured fabric materials can be again categorized into 3 types namely, Uniform texture, Random texture and Patterned texture. In this project Uniform Textured Fabrics of Polyster and Cotton fabrics are considered.

<img src= "https://github.com/PrimeshShamilka/fabric_defect_detector/blob/master/images/Design/fabric_types.png" width="400">

<br/>


### Motivation behind autonomous fabric defect detection

* Manual inspection is erroneous
* 30% of defects are missed out due to human error
* Low inspection speed of around 8 m/min in manual inspection
* Concentration time of a quality control employee is limited to 20-30 minutes
* Only 10% of the rolls are inspected

// manual inspection image

<br/>



## OUR SOLUTION

### **We have introduced a Real time Autonomous Fabric Stain Detection method using the latest computer vision technologies. Our defect detection pipeline is based on the state of the art YOLOv3 object detecor.**

## This repository includes,

- google colab ipython files of defect deteciton models that were developed
- configurations files of the relavant models
- image pre-processing module 
- OpenCV python API for YOLOv3
- helper module scripts
- other resource files for darknet framework

<br/>

## SYSTEM DESIGN

### Abstract view of the system

### Architecture of a typical web inspection system

### State chart diagram
<img src="https://github.com/PrimeshShamilka/fabric_defect_detector/blob/master/images/Design/Abstract.png" width="400">

<br/>


## STAIN DETECTION MODULE

Stain detection module consists of 4 sub modules,
* Image acquisition module
* Image preprocessing module
* Feature extraction module
* Stain localization & classification module

// pipeline image

We have used YOLO object detector to implement the feature extraction module and stain localization and classification module. YOLO uses a Deep Convolutional Nueral Network as the feature extractor. Architecture of the YOLOv3 object detector is given below.

// YOLOv3 architecture

<br/>

## TRAINING THE STAIN DETECTION MODEL

Implementing the stain detection model was carried out in a circular method. Implementing, Evaluating and Improving circular methodology was used to build the optimum model. According to the circular process 6 models were built and each successor model is an improved version of its predecessor. Reference dataset was used to evaluate each model and feedback from each model was used to improve its successor.  

### Reference dataset - TILDA textile texture dataset

* 8 different textile types
* 7 error classes for each textile type
* 50 TIF images for each class (768x512 pixel, graylevel image 8 bit)
* 3200 TIF images in total
* Stain images from TILDA dataset were used
* 187 stain defect images
* 151 defect free images

### Learning curves

// image


### Model summary
// image

<br/>

## TECHNIQUES USED TO IMPROVE MODEL ACCURACY

### IMAGE PREPROCESSING 
* Histogram analysis (Contrast Limited Adaptive Histogram Equalization - CLAHE)
* Gaussian noise removal filtering
* Standardizing image data
* Resizing images
* Image augmentation

### BIAS & VARIANCE TRADE-OFF ANALYSIS
* TRAIN/VALID/TEST SPLIT (70%,15%,15%)
* Reducing underfitting & overfitting (low bias & low variance)

### HYPERPARAMETER TUNING
* Learning rate
* No. of iterations
* Input resolution
* Optimization algorithm 
* Batch size

### USING DIFFERENT MODEL ARCHITECTURES
* YOLOv3 
* YOLOv3 - tiny - 3 yolo layers
* YOLOv3_5l - 5 yolo layers
* YOLOv3-spp - with spatial pyramid pooling
* YOLOv4 - 3 yolo layers

<br/>

## VALIDATING THE MODEL USING A CUSTOM DATASET

In order to further validate the model on unseen data a custom stain dataset of 398 stain images and 68 defect_free images was created. This dataset is publically avaialble on kaggle under CC0:Public Domain Liscenece and you can download it from the link below.

// datset link

### Stain size distribution between the reference dataset and the custom dataset


Dataset was preprocessed using the preprocessing model. Model was trained on the custom dataset in 3 approaches and the optimum approach was selected for further improvements.

// approaches image

<br/>


## DIMENSION CLUSTERING OF TARGET FRAMES TO DETERMINE THE SIZE AND NUMBER OF ANCHOR BOXES(PRIOR BOXES)

To further improve the accuracy of the model on the custom dataset cluster analysis was done usin K-mean clustering algorithm to find out the optimum sizes and number of anchor boxes for YOLOv3 object detector. 

// cluster analysis image


## RESULTS









## YOLOv3 OpenCV python API documentation



## Helper modules


## REFERENCES





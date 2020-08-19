# FABRIC STAIN DETECTION USING YOLOv3

## CONTENTS

- [Demo](https://github.com/PrimeshShamilka/fabric_defect_detector/blob/master/README.md#demo)
- [1. Problem definition](https://github.com/PrimeshShamilka/fabric_defect_detector#problem)
- [2. Proposed solution](https://github.com/PrimeshShamilka/fabric_defect_detector#our-solution)
- [3. System design](https://github.com/PrimeshShamilka/fabric_defect_detector#system-design)
- [4. Stain detection module](https://github.com/PrimeshShamilka/fabric_defect_detector#stain-detection-module)
- [5. Training the model](https://github.com/PrimeshShamilka/fabric_defect_detector#training-the-stain-detection-model)
- [6. Techniques used to improve the model accuracy](https://github.com/PrimeshShamilka/fabric_defect_detector#techniques-used-to-improve-model-accuracy)
- [7. Validating the model using a custom dataset](https://github.com/PrimeshShamilka/fabric_defect_detector#validating-the-model-using-a-custom-dataset)
- [8. Dimension clustering of target frames to determine the size and number of anchor boxes](https://github.com/PrimeshShamilka/fabric_defect_detector#dimension-clustering-of-target-frames-to-determine-the-size-and-number-of-anchor-boxesprior-boxes)
- [9. Results](https://github.com/PrimeshShamilka/fabric_defect_detector#results)
- [10. References](https://github.com/PrimeshShamilka/fabric_defect_detector#references)

<br/>

## DEMO

<a href="http://www.youtube.com/watch?feature=player_embedded&v=WDOfIpKW65c
" target="_blank"><img src="http://img.youtube.com/vi/WDOfIpKW65c/0.jpg" 
alt="" width="480" height="360" border="1" /></a>

<br/>

### How to run?

#### For Linux 

- Run the following commands in a terminal

```
   git clone https://github.com/AlexeyAB/darknet.git
   cd darknet
   make
```

- Donwload the configuration file of the model from the link below and copy it to cfg directory inside darknet root directory \
  https://drive.google.com/file/d/12ikV938ZEXWjoITYW6mE0FqoZQbyET1v/view?usp=sharing
  
- Download obj.data, classes.names files from the links below and copy them to data directory inside darknet root directory
  obj.data file - https://drive.google.com/file/d/1B54Q4VQjlHVkLoQb132EgBjyEJ0lJ0yy/view?usp=sharing \
  classes.names file - https://drive.google.com/file/d/1WBVQI6e0p7TQtTExXbRUcwaG5N9A9xwL/view?usp=sharing

- Download the trained weight file for the model from the link below and copy the weights to backup directory inside darknet root directory \
  https://drive.google.com/file/d/18GULkIGA2Qpg4rfYbp2moGaZLoxtjuAw/view?usp=sharing

- Test on a video feed

``` 
  ./darknet detector demo data/obj.data cfg/custom.cfg backup/stain_detection_model.weights test.mp4 
```


<br/>

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

<img src="https://github.com/PrimeshShamilka/fabric_defect_detector/blob/master/images/Design/motivation.png" width="400">

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
<img src="https://github.com/PrimeshShamilka/fabric_defect_detector/blob/master/images/Design/mount.png" width="400">


### Architecture of a typical web inspection system
<img src="https://github.com/PrimeshShamilka/fabric_defect_detector/blob/master/images/Design/architecture_typical_design.png" width="400">


### State chart diagram
<img src="https://github.com/PrimeshShamilka/fabric_defect_detector/blob/master/images/Design/Abstract.png" width="400">

<br/>


## STAIN DETECTION MODULE

Stain detection module consists of 4 sub modules,
* Image acquisition module
* Image preprocessing module
* Feature extraction module
* Stain localization & classification module

<img src="https://github.com/PrimeshShamilka/fabric_defect_detector/blob/master/images/Design/computer_vision_pipeline.png" width="600">

We have used YOLO object detector to implement the feature extraction module and stain localization and classification module. YOLO uses a Deep Convolutional Nueral Network as the feature extractor. Architecture of the YOLOv3 object detector is given below.

<img src="https://github.com/PrimeshShamilka/fabric_defect_detector/blob/master/images/Design/yolo_archi.png" width="600">

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

<img src="https://github.com/PrimeshShamilka/fabric_defect_detector/blob/master/images/Design/learning_curves.png" width="600">



### Model summary
<img src="https://github.com/PrimeshShamilka/fabric_defect_detector/blob/master/images/Design/model_summary.png" width="600">


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

FABRIC STAIN DATASET - https://www.kaggle.com/priemshpathirana/fabric-stain-dataset

### Stain size distribution between the reference dataset and the custom dataset
<img src="https://github.com/PrimeshShamilka/fabric_defect_detector/blob/master/images/Design/stain_size_distribution.png" width="600">


Dataset was preprocessed using the preprocessing model. Model was trained on the custom dataset in 3 approaches and the optimum approach was selected for further improvements.

<img src="https://github.com/PrimeshShamilka/fabric_defect_detector/blob/master/images/Design/custom_dataset_approach.png" width="600">


<br/>


## DIMENSION CLUSTERING OF TARGET FRAMES TO DETERMINE THE SIZE AND NUMBER OF ANCHOR BOXES(PRIOR BOXES)

To further improve the accuracy of the model on the custom dataset cluster analysis was done usin K-mean clustering algorithm to find out the optimum sizes and number of anchor boxes for YOLOv3 object detector. 

<img src="https://github.com/PrimeshShamilka/fabric_defect_detector/blob/master/images/Design/Average%20IoU%20vs.%20Number%20of%20clusters.png" width="400">


## RESULTS

<img src="https://github.com/PrimeshShamilka/fabric_defect_detector/blob/master/images/Results/overall_results.png" width="600">


## REFERENCES

- Ajay Kumar, “Computer Vision-Based Fabric Defect Detection: A Survey” , Jan 2001
- Hong-wei Zhang , Ling-jie Zhang , Peng-fei Li , De Gu, “Yarn-dyed Fabric Defect Detection with YOLOV2 Based on Deep Convolutional Neural Networks”, Xi'an Polytechnic University, May 2018
- Junfeng Jing , Dong Zhuo, Huanhuan Zhang, Yong Liang and Min Zheng, “Fabric defect detection using the improved YOLOv3 model”, Jan 2020
- Jun-Feng Jing, Hao Ma and Huan-Huan Zhang, “Automatic fabric defect detection using a deep convolutional neural network”, School of Electronics and Information, Xi’an Polytechnic University, Feb 2019
- Joseph Redmon, Ali Farhadi, “YOLOv3: An Incremental Improvement”, University of Washington
- Cihat Okan Arıkan, “Developing an Intelligent Automation and Reporting System for Fabric Inspection Machines”,Ege University, Department of Textile Engineering, 2019




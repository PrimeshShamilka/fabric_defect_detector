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


## SYSTEM DESIGN

### Abstract view of the system

### Architecture of a typical web inspection system

### State chart diagram
<img src="https://github.com/PrimeshShamilka/fabric_defect_detector/blob/master/images/Design/Abstract.png" width="400">


## High Level computer vision pipeline of the system

<img src="https://github.com/PrimeshShamilka/fabric_defect_detector/blob/master/images/Design/architecture%20pipeline.jpeg" width="900">

<img src="https://github.com/PrimeshShamilka/fabric_defect_detector/blob/master/images/Design/nueral%20network%20architecture%20NEW.png" width="900">


## Why YOLO?

![](https://github.com/PrimeshShamilka/fabric_defect_detector/blob/master/images/Design/model_comparison.png)

![](https://github.com/PrimeshShamilka/fabric_defect_detector/blob/master/images/Design/yolo_architecture.png)



## Stain defect detection results of TILDA dataset

TILDA dataset was used as the reference dataset to develop, improve and validate the performance of the model. 


## Stain defect detection results of a custom dataset



## YOLOv3 OpenCV python API documentation



## Helper modules





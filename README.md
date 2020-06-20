# fabric_defect_detector

## Fabric defect detector using YOLOv3

Fabric quality control is very important in textile industry. However, due to problems of equipment failure and worker's   fatigue, fabric surface defects are inevitable. The efficiency of traditional manual method is low and the missrate is high due to subjectivity and other shortcoming. Thus an automation fabric defect detection is necessary for textile industry. 

In industrial fabrics there are around  60 fabric defect types. Amongs these fabric defect types stain is the most abundant fabric defect. Basically, fabric materials can be categorized into two categories as Textured material and Uniform material. Textured fabric materials can be again categorized into 3 types namely, Uniform texture, Random texture and Patterned texture. In this project only Uniform textured fabrics are considered.

We have introduced an autonomous fabric stain detection method is introduces using the latest computer vision technologies. Our defect detection pipeline is based on the state of the art YOLOv3 object detecor. 

### This repository provides,
- google colab ipython files of defect deteciton models that were developed
- configurations files of the relavant models
- image pre-processing module 
- OpenCV python API for YOLOv3
- helper module scripts

## Fabric types & Fabric defects

// images

## System Design

// images

The basic computer vision pipeline of our system is given below. 

// architecture images

## Why YOLO?

TILDA dataset was used as the reference dataset to develop, improve and validate the performance of the model. 







## Stain defect detection results of TILDA dataset



## Stain defect detection results of a custom dataset



## YOLOv3 OpenCV python API documentation



## Helper modules





# RPi Camera Carplate Worker

... work in progress ...

A project where I use Raspberry Pi as a smart camera to detects car plates. The idea behind is to detect cars car plate (e.g. in front yard/close to garage door), recognize characters and make some action, based on if the car plate on detected car are from your car or someone elses. 

## Hardware & equipment

List of stuff in my setup:
* Raspberry Pi 4 (+ power supply, SD card)
* Rasspberry Pi High Quality Camera module
* junction box (as a computer enclosure)
* camera stand
* M42 Mount to C-Mount Screw Lens
* M42 lens


## Software

Very useful repositories and links also used during my project:
* [RPi_Cam_Web_Interface](https://github.com/silvanmelchior/RPi_Cam_Web_Interface)
* [
TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10](https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10)
* [TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi](https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi)


## Steps

### 1. Train dataset acquisition

After setting up Raspberry Pi OS, enabling camera, positioning everything to the desired location in my house, the first step for this project I count as train dataset acquisition. We need this dataset to make our own model for recognizing car plates.

Train dataset in this case are the images of cars. In my case, the tool that I used for this is [_RPi_Cam_Web_Interface_](https://github.com/silvanmelchior/RPi_Cam_Web_Interface). After installing, I enabled motion detector and waited until I had few hundred videos saved in detections history.

### 2. Train model

This part is well described here - [
_TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10_](https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10).

In short - I downloaded videos, that were detected in previous step, to my main computer (Windows 10) with WinSCP, manualy made screenshots of multiple car positions and labeled them with LabelImg. The rest of the upper guide goes step by step with procedure how to train tensorflow model.

Model that was used in this project - ssd_mobilenet_v2_quantized_300x300_coco_2019_01_03

This model needs to be transformed to TFlite model, which can later be used in Raspberry Pi (look at this for more detailed guide - [_TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi_](https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi)).
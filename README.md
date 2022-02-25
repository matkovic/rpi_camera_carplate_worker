# RPi Camera Carplate Worker

... work in progress ...

A project where I use Raspberry Pi as a smart camera to detects car plates. The idea behind is to detect cars car plate (e.g. in front yard/close to garage door), recognize characters and make some action, based on if the car plate on detected car are from your car or someone elses. The action that can be triggered is in this case triggering RF signal to open garage door (or RF wireless bell).

## Hardware & equipment

List of stuff in my setup:
* Raspberry Pi 4 (+ power supply, SD card)
* Rasspberry Pi High Quality Camera module
* junction box (as a computer enclosure)
* camera stand
* M42 Mount to C-Mount Screw Lens
* M42 lens
* RF (433) wireless bell


## Software

Very useful repositories and links also used during my project:
* [RPi_Cam_Web_Interface](https://github.com/silvanmelchior/RPi_Cam_Web_Interface)
* [
TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10](https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10)
* [TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi](https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi)
* [rpitx](https://github.com/F5OEO/rpitx)
* [sqlite-web](https://github.com/coleifer/sqlite-web)


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

### 3. Detect car plates in action

With the result of previous step, now we can use our model to detect car plates in front of our house.

Here comes _RPi_Cam_Web_Interface_ and in combination with [previous tutorial](https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi)'s script, now we can constantly use our model for car plate detection via video stream (from RPI Cam Web Interface) or directly on camera without intermediary step.

Now I do not want to do the latter, since constantly checking if there is any car plate in camera view using our TFLite model heats up our Raspberry Pi. A compromise that I decided for is to use _RPi_Cam_Web_Interface_'s motion detector and start the TFLite model script (reading via http video stream) when the motion starts and end (kill the process) when the motion ends.

### 4. Log data

Log data that was detected in previous step by saving it to folder structure and some mini database (sqlite) on the RPi.

### 5. Trigger action

If some specific data was detected in the previous step, now we can trigger RF signal using *rpitx*'s `sendiq` script.

---

## Setup stuff

Create folder for saving detected images in www folder to be accessible through browser and allow nologin user to make new files here:
```
mkdir /var/www/imgs/
sudo chmod o+rwx /var/www/imgs/
```

*RPi-Cam-Web-Interface* - enable motion detection on startup:
```
sudo vim /etc/raspimjpeg
```
Edit this line
```
motion_detection true
```


*Sudoers* allow nologin to run rpitx script:
```
sudo visudo
```
Add this inside
```
#custom
www-data ALL=NOPASSWD: /home/pi/rpitx/sendiq
```

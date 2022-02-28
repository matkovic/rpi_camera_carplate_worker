# Raspberry Pi object detection

The [TFLite_detection_stream_ed.py](./TFLite_detection_stream_ed.py)'s code is mostly from here - [TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi](https://github.com/EdjeElectronics/TensorFlow-Lite-Object-Detection-on-Android-and-Raspberry-Pi).

The [motion_event.sh](./motion_event.sh) is required by RPi_Cam_Web_Interface's motion detection module, which is run everytime when a motion is detected or ended. File is located in `/var/www/html/macros/` (or wherever you have your RPi_Cam_Web_interface installed).


Commands for installing python environment requirements:

```
sudo apt install tesseract-ocr -y
python3 -m venv tflite1-env
source tflite1-env/bin/activate
pip install -r requirements.txt
```


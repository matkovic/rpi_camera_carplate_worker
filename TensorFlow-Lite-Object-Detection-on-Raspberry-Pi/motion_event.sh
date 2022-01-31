#!/bin/bash

if [ $1 = '1' ]
then
	source /home/pi/tflite1/tflite1-env/bin/activate
	python3 /home/pi/tflite1/TFLite_detection_stream_ed.py --streamurl http://127.0.0.1:8080/html/cam_pic_new.php --modeldir /home/pi/tflite1/TFLite_model_carplate --resolution 512x288 &
elif [ $1 = '0' ]
then
	pkill -f TFLite_detection_stream_ed.py
fi

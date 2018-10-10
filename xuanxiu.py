import os
import cv2
import numpy as np
import time

adb='/Users/sakurauchiriko/Desktop/platform-tools/adb'

def sleeptime(hour,min,sec):
	return hour*3600 + min*60 + sec

def acc():
	os.system(adb+' shell input tap 1400 700')
	os.system(adb+' shell input tap 1319 1025')
	second = sleeptime(0,0,0.5)
	time.sleep(second)
	os.system(adb+' shell input tap 1319 1025')
	os.system(adb+' shell input tap 1400 700')

def start_to_play():
	second = sleeptime(0,0,1)
	time.sleep(second)
	os.system(adb+' shell input tap 1400 700')
	os.system(adb+' shell input tap 897 570')

def answer():
	os.system(adb+' shell input tap 330 371')
	print('option clicked')
	os.system(adb+' shell input tap 1543 143')
	print('close clicked')

def pull_screenshot(num):
    os.system(adb+' shell screencap -p /sdcard/screenshot'+num+'.png')
    os.system(adb+' pull /sdcard/screenshot'+num+'.png '+'/Users/sakurauchiriko/Desktop/pics/screenshot'+num+'.png')
    os.system(adb+' shell rm /sdcard/screenshot'+num+'.png')

def check_screenshot():
	pull_screenshot('1')
	second = sleeptime(0,0,3)
	time.sleep(second)
	pull_screenshot('2')
    
def judge():
	image1=cv2.imread('/Users/sakurauchiriko/Desktop/pics/screenshot1.png')
	print('1 read success')
	image2 = cv2.imread('/Users/sakurauchiriko/Desktop/pics/screenshot2.png')
	print('2 read success')
	dif= cv2.subtract(image1,image2)
	result= not np.any(dif)
	print('compare success '+str(result))
	if result == True:
		print('same')
		answer()
		start_to_play()
		acc()
		delete_pics()
		
	else:
		print('not same')
		delete_pics()

def delete_pics():
	os.system('rm /Users/sakurauchiriko/Desktop/pics/screenshot1.png')
	os.system('rm /Users/sakurauchiriko/Desktop/pics/screenshot2.png')

def main():
	os.system(adb+' shell settings put global policy_control immersive.status=*')
	while 1==1:
		check_screenshot()
		judge()
	

if __name__ == '__main__':
	main()

		
	
	
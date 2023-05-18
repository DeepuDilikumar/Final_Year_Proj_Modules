import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def activate_youtube_controls(website_url):

	#Initialize Firefox driver
	driver = webdriver.Firefox()
	driver.get(website_url)
	
	#wait for the video player to load
	time.sleep(3)
	
	#finding the video element
	video = ''
	try:
		video = driver.find_element('css selector', 'video.html5-main-video')
		#print('Video variable value: ', video)
		print('Video element got successfully!')

	except Exception as e:
		print('Error occured while getting the video element!')
		print(e)
		sys.exit()
		
	
	print("""
		Entered to Youtube Video Control Section. Just say exit to quit controlling the video!
	""")
	command = input('Enter what you want to do with video: ')
	while command != 'exit':
		try:
			if 'pause' in command:
				video.send_keys('k')
				print('Video Paused')

			elif 'play' in command:
				video.send_keys('k')
				print('Playing Video')

			elif 'skip ad' in command:
				skip_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'ytp-ad-skip-button')]")))
				skip_button.click()
				print('Ad Skipped')
			
			elif 'forward' in command:
				video.send_keys(Keys.ARROW_RIGHT)
				print('Video Forwarded')
			
			elif 'backward' in command:
				video.send_keys(Keys.ARROW_LEFT)
				print('Video Backward')
			
			elif 'full screen' in command:
				video.send_keys('f')
				print('Full Screen Activated')

			elif 'normal screen' in command:
				video.send_keys('f')
				print('Back to normal screen')

			elif 'increase speed' in command:
				video.send_keys(Keys.SHIFT, '>')
				time.sleep(1)
				print('Video Speed Increased')

			elif 'decrease speed' in command:
				video.send_keys(Keys.SHIFT, '<')
				time.sleep(1)
				print('Video speed increased')
				
			elif 'increase volume' in command:
				video.send_keys(keys.ARROW_UP);
				time.sleep(1);
				print('Volume increased');
				
			elif 'decrease volume' in command:
				video.send_keys(keys.ARROW_DOWN);
				time.sleep(1);
				print('Volume decreased');
			
			else:
				print('Sorry, could not understand your command!')
		
		except Exception as e:
			print('Some error occured while carrying out the execution!')

		command = input('Enter what you want to do with video: ')
	
	want_to_close_yt_video = input('Do you want to close youtube video as well? (Just say yes or no): ')
	if 'yes' in want_to_close_yt_video:
		driver.quit()


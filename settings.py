import os
import random
from PIL import Image


PATH = 'images'
OUT_PATH = 'output'

IMG_SIZE = (32, 32)

LAYER_RARITIES = (
	1.0,	# color
	0.3,	# second color
	0.001,	# special
	1.0,	# eyes
	0.1,	# second eye
	0.9,	# paws
	0.5,	# neckband
	0.2,	# top
	0.3,	# bottom
)

BGS = {
	'0-82': (120, 150, 180),	# blue		# Common
	'82-92': (117, 191, 128),	# green		# Rare
	'92-98': (142, 111, 182),	# purple	# Epic
	'98-99.9': (255, 225, 150),	# yellow	# Leggendary
	'99.9-100': (179, 85, 79),	# red		# Supreme
}


EXCEPTIONS = {
	'images\\0_color\\color_0.png': [
		'images\\3_eyes\\eyes_5.png',
		'images\\4_second_eye\\eye_5.png',
		'images\\5_paws\\paws_0.png',
		'images\\5_paws\\paws_2.png',
		'images\\5_paws\\paws_3.png',
		'images\\5_paws\\paws_4.png',
		'images\\5_paws\\paws_5.png',
		'images\\5_paws\\paws_6.png',
		'images\\5_paws\\paws_7.png',
	],
	'images\\0_color\\color_1.png': [
		'images\\5_paws\\paws_0.png',
		'images\\5_paws\\paws_2.png',
		'images\\5_paws\\paws_4.png',
		'images\\5_paws\\paws_5.png',
		'images\\5_paws\\paws_6.png',
		'images\\5_paws\\paws_7.png',
	],
	'images\\0_color\\color_2.png': [
		'images\\3_eyes\\eyes_0.png',
		'images\\3_eyes\\eyes_1.png',
		'images\\4_second_eye\\eye_0.png',
		'images\\4_second_eye\\eye_1.png',
		'images\\5_paws\\paws_2.png',
		'images\\5_paws\\paws_3.png',
		'images\\5_paws\\paws_5.png',
		'images\\5_paws\\paws_6.png',
		'images\\5_paws\\paws_7.png',
	],
	'images\\0_color\\color_3.png': [
		'images\\3_eyes\\eyes_2.png',
		'images\\4_second_eye\\eye_2.png',
		'images\\5_paws\\paws_0.png',
		'images\\5_paws\\paws_2.png',
		'images\\5_paws\\paws_3.png',
		'images\\5_paws\\paws_4.png',
		'images\\5_paws\\paws_6.png',
		'images\\5_paws\\paws_7.png',
	],
	'images\\0_color\\color_4.png': [
		'images\\3_eyes\\eyes_0.png',
		'images\\4_second_eye\\eye_0.png',
		'images\\5_paws\\paws_0.png',
		'images\\5_paws\\paws_1.png',
		'images\\5_paws\\paws_2.png',
		'images\\5_paws\\paws_3.png',
		'images\\5_paws\\paws_4.png',
		'images\\5_paws\\paws_7.png',
		'images\\5_neckband\\neckband_07.png',
	],
	'images\\0_color\\color_5.png': [
		'images\\3_eyes\\eyes_4.png',
		'images\\4_second_eye\\eye_4.png',
		'images\\5_paws\\paws_0.png',
		'images\\5_paws\\paws_2.png',
		'images\\5_paws\\paws_3.png',
		'images\\5_paws\\paws_4.png',
		'images\\5_paws\\paws_5.png',
		'images\\5_paws\\paws_6.png',
	],
	'images\\2_special\\special_0.png': [
		'images\\3_eyes\\eyes_1.png',
		'images\\3_eyes\\eyes_5.png',
		'images\\4_second_eye\\eye_1.png',
		'images\\4_second_eye\\eye_5.png',
	],
}


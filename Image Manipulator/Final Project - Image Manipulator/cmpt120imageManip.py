# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s):
# Date:
# Description:

import cmpt120imageProj
import numpy


pixels = cmpt120imageProj.getImage('project-photo.jpg')
width = len(pixels)
height = len(pixels[0])

# return the original image array
def original():
	return cmpt120imageProj.getImage('project-photo.jpg')


# invert image
def invert(pixels):
	img = pixels
	for col in range(width):
		for row in range(height):
			# change the value to be inverted
			img[col][row] = [(255-pixels[col][row][0]),(255-pixels[col][row][1]),(255-pixels[col][row][2])]
	return img
	# cmpt120imageProj.showImage(img, 'Invert')


# flip image horizontally
def flipH(pixels):
	pixels = pixels
	img = []

	# itterate the list backwards
	for col in range(width-1,-1,-1):
		img.append(pixels[col])
	return img





# flip image vertically
def flipV(pixels):
	new_img = cmpt120imageProj.createBlackImage(600,400)

	for col in range(width):
		temp = []
		# add values to temp in reverse
		for row in reversed(pixels[col]):
			temp.append(row)

		# replace list with a reversed
		new_img[col] = temp

	return new_img






# removes red channel
def remove_red_channel(pixels):

	img = pixels.copy()
	# iterate through list
	for col in range(width):
		for row in range(height):
			# remove red channel
			img[col][row] = [0,pixels[col][row][1],pixels[col][row][2]]
	return img





# remove gren remove_red_channel
def remove_green_channel(pixels):

	# make a copy
	img = pixels.copy()

	# parse the pixels
	for col in range(width):
		for row in range(height):

			# remove blue by setting b value to 0
			img[col][row] = [(pixels[col][row][0]),0,(pixels[col][row][2])]
	return img



# remove blue channel
def remove_blue_channel(pixels):

	img = pixels.copy()

	for col in range(width):
		for row in range(height):

			# remove green value by setting g value to 0
			img[col][row] = [(pixels[col][row][0]),(pixels[col][row][1]),(0)]
	return img



# convert to greyscale
def greyscale(pixels):
	img = pixels
	for col in range(width):
			for row in range(height):

				# collect rgb values
				r = pixels[col][row][0]
				g = pixels[col][row][1]
				b = pixels[col][row][2]

				# get the average of those values
				avg = (r+g+b)/3

				# set rbg values equals to average of the values
				img[col][row] = (avg, avg, avg)
	return img


# apply sepia filter
def apply_sepia_filter(pixels):
	img = pixels
	for col in range(width):
			for row in range(height):

				# collect the rbg values for each pixel
				r = pixels[col][row][0]
				g = pixels[col][row][1]
				b = pixels[col][row][2]


				# calculate the rgb values with the sapia functions
				tr = int(0.393*r + 0.769*g + 0.189*b)
				tg = int(0.349*r + 0.686*g + 0.168*b)
				tb = int(0.272*r + 0.534*g + 0.131*b)

				# make sure they dont exceed 255
				if(tr > 255):
				    r = 255
				else:
				    r = tr

				if(tg > 255):
				    g = 255
				else:
				    g = tg

				if(tb > 255):
				    b = 255
				else:
				    b = tb

				img[col][row] = (r, g, b)
	return img


# decrease brightness
def decrease_brightness(pixels):

	img = pixels

	for col in range(width):
			for row in range(height):

				# collect the rgb values
				r = pixels[col][row][0]
				if r > 10:
					r = r-10
				g = pixels[col][row][1]
				if g > 10:
					g = g-10
				b = pixels[col][row][2]
				if b > 10:
					b = b-10

				# make the values less intense
				img[col][row] = (r, g, b)

	return img



def increase_brightness(pixels):
# increase brightness

	img = pixels

	for col in range(width):
			for row in range(height):

				# collect the rgb values
				r = pixels[col][row][0]
				if r < 245:
					r = r + 10
				g = pixels[col][row][1]
				if g < 245:
					g = g + 10
				b = pixels[col][row][2]
				if b < 245:
					b = b + 10
				
				# set the rbg values
				img[col][row] = (r, g, b)

	return img


	# binarize
def binarize(pixels):
# increase brightness

	img = pixels

	# parse the pixels
	for col in range(width):
			for row in range(height):

				# collect the rgb values
				r = pixels[col][row][0]
				g = pixels[col][row][1]
				b = pixels[col][row][2]


				# make sure the values dont exceed 255
				if b > 136:
					r = 255
					b = 255
					g = 255
				else:
					r = 0
					b = 0
					g = 0
				
				# set the rbg values
				img[col][row] = (r, g, b)

	return img

# ROTATE IMAGE 90 DEGREE LEFT
def rotate_left(pixels):

	# get mesurements of the image
	width = len(pixels)
	height = len(pixels[0])

	# create a canvas
	img = cmpt120imageProj.createBlackImage(height,width)


	for i in range(width):
		for j in range(height):
			pixel = pixels[i][j]
			# replace pixels in the opposite ends
			pixels[i][j] = img[j][width-i-1]
			img[j][width-i-1] = pixel

	return img


def rotate_right(pixels):

	# get mesurements
	width = len(pixels)
	height = len(pixels[0])

	# create a canvas
	img = cmpt120imageProj.createBlackImage(height,width)

	for i in range(width):
		for j in range(height):
			pixel = pixels[i][j]
			# replace pixels in the opposite ends
			pixels[i][j] = img[height-j-1][i]
			img[height-j-1][i] = pixel

	return img



def pixelate(pixels):

	# get width and height of the picture
	width = len(pixels)
	height = len(pixels[0])

	# parse by 4
	for x in range(0,width,+4):
		for y in range(0,height, +4): 

			# sum of the rbg values
			rsum = 0
			gsum = 0
			bsum = 0

			# collect the rbg values on a 4 by 4 scale
			for i in range(4):
				rsum = rsum + pixels[x][y+i][0]
				gsum = gsum + pixels[x][y+i][1]
				bsum = bsum + pixels[x][y+i][2]

			for i in range(4):
				rsum = rsum + pixels[x][y+i][0]
				gsum = gsum + pixels[x][y+i][1]
				bsum = bsum + pixels[x][y+i][2]

			for i in range(4):
				rsum = rsum + pixels[x][y+i][0]
				gsum = gsum + pixels[x][y+i][1]
				bsum = bsum + pixels[x][y+i][2]

			for i in range(4):
				rsum = rsum + pixels[x][y+i][0]
				gsum = gsum + pixels[x][y+i][1]
				bsum = bsum + pixels[x][y+i][2]


			# get the average of the values
			ravg = rsum/16
			gavg = gsum/16
			bavg = bsum/16

			# replace the rbg values with the average values
			for i in range(4):
				pixels[x][y+i] = [ravg,gavg,bavg]

			for i in range(4):
				pixels[x+1][y+i] = [ravg,gavg,bavg]

			for i in range(4):
				pixels[x+2][y+i] = [ravg,gavg,bavg]

			for i in range(4):
				pixels[x+3][y+i] = [ravg,gavg,bavg]

	return pixels
import PIL
from PIL import Image

def main (image):

	width_im, height_im = image.size

	check_within(width_im, height_im)


def crop_photo (image, w, h):
	# 3 sizes
	square_image = (0,0,1080,1080)
	ver_image = (0,0,1080,1350)
	hori_image = (0,0,1080,566)

	width_im, height_im = image.size

	type = check_type(width, height)

	if (type == 'hori'):
		make_horizontal 
	elif (type == "ver"):
		make_vertical
	else:
		make_square


def check_type(width, height):

	if (width > height):
		return 'hori'
	elif (width < height):
		return 'ver'
	else:
		return 'square'

'''def make_horizontal(img):
	baseheight = 566
	hpercent = (baseheight / float(img.size[1]))
	wsize = int((float(img.size[0]) * float(hpercent)))
	resize_img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
	print (hpercent, wsize)
	new_width, new_height = resize_img.size
	print (new_width)
	cropped_img = resize_img.crop(((new_width/2+540), 233, 1080, 566))

	img.save("test1.jpg")'''

def test (i):
	w,h = i.size
	ratio = min(1080/w, 566/h)
	size = w,h*ratio

	i.thumbnail((size), Image.ANTIALIAS)
	i.save("test1.jpg")

img = Image.open("test.jpg")
test (img)



	



	






from PIL import Image

image = Image.open('IMAGE.jpg')
image_red, image_green, image_blue = image.split()

bias = 80

coordinates_for_crop_left = (bias, 0, image.width, image.height)
coordinates_for_crop_right = (0 , 0, image.width - bias, image.height)
coordinates_for_crop_half = (bias / 2, 0,
                             image.width - bias / 2, image.height)

image_red_crop = image_red.crop(coordinates_for_crop_left)
image_red_crop2 = image_red.crop(coordinates_for_crop_half)

image_blue_crop = image_blue.crop(coordinates_for_crop_right)
image_blue_crop2 = image_blue.crop(coordinates_for_crop_half)

image_green_crop2 = image_green.crop(coordinates_for_crop_half)

image_red_blend = Image.blend(image_red_crop, image_red_crop2, 0.3)
image_blue_blend = Image.blend(image_blue_crop, image_blue_crop2, 0.3)

image_rgb = Image.merge('RGB',
                        (image_red_blend, image_green_crop2, image_blue_blend))
image_rgb.save('IMAGE_RGB.jpg')

image_rgb.thumbnail((80, 80))
image_rgb.save('IMAGE_thumbnail.jpg')

from PIL import Image

def concat_img(padding, im1, im2, im3, im4, im5, im6, color=(255, 255, 255)):
    new_img = Image.new('RGB', (im1.width * 4 + padding * 2, im1.height * 3 + padding * 2), color)
    new_img.paste(im1, (im1.width + padding, im1.height + padding))
    new_img.paste(im2, ((im1.width * 3) + padding, im1.height + padding))
    new_img.paste(im3, (im1.width + padding, im1.height * 2 + padding))
    new_img.paste(im4, ((im1.width * 2) + padding, im1.height + padding))
    new_img.paste(im5, (im1.width + padding, 0 + padding))
    new_img.paste(im6, (0 + padding, im1.height + padding))
    return new_img
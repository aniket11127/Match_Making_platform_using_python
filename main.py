import glob
# The glob module, which is short for global, is a function that's used to search for files that match a specific file pattern or name


import imagehash
# Image hashes module tells whether two images look nearly identical by computing their hash numbers.


from PIL import Image
# To load the image, we simply import the image module from the pillow ie PIL


boy_img_url = "./boys/rock.jpg"    # Note : rdj.jpg is the jpg file of the boy
boy_hash = imagehash.average_hash(Image.open(boy_img_url))
j = glob.glob("./girls/*.jpg")    # Note : Here girls is the name of the folder where girls images are there
selected = j[0]
accepted_diff = 1000
for i in j:
    girl_hash = imagehash.average_hash(Image.open(i))
    diff = girl_hash - boy_hash
    if diff < accepted_diff:
        selected = i
        accepted_diff = diff
        
        
boy_img = Image.open(boy_img_url)
girl_img = Image.open(selected)
final_img = Image.new('RGB', (boy_img.width + girl_img.width, boy_img.height))
#RGB (red, green and blue) refers to a system representing the colours used on a digital display screen
final_img.paste(boy_img, (0, 0))
final_img.paste(girl_img, (boy_img.width, 0))
final_img.save('Final_Frame.jpg')
final_img.show()
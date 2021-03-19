import cv2
import matplotlib.pyplot as plt
import numpy as np
from faker import Faker
import random
import io
from random import choice
from string import digits
from PIL import Image
from urllib.request import Request, urlopen
#global
global shape,font,fontScale,color,thickness
shape = (412,266)
image_shape = (111,111)
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 0.5
color = (0, 0, 0)
thickness = 2
image_url = "https://thispersondoesnotexist.com/image"
my_list =["CAR","MOTORCYCLE"]
my_con =["S","N"]

#faker invocation
fake = Faker()

#function to resize images

def resize(image, con):
    if con =="license":
        resized_image =cv2.resize(image, shape)
    if con == "photo":
        resized_image = cv2.resize(image, image_shape)
    return resized_image

def download_image(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = np.array(urlopen(req).read())
    img = np.asarray(Image.open(io.BytesIO(webpage)))
    return img


def rangen():
    m = (''.join(choice(digits) for i in range(9)))
    return m

def ranien():
    y = (''.join(choice(digits) for i in range(4)))
    return y

# co-ordinates
name_l = (18,70)  #name
address_l = (18,110)   #addline1
address_l2 =(18,130) #addline2
license_num = (315,70)  # num
license_exp =(18,160) #date
dob = (147,160)   #date
license_type = (18,195) #car,bike
condition = (145,195)  #S or N
image =()

#DP
temp = np.asarray(plt.imread("lic_temp.jpeg")) # template
temp_1 = temp.copy()
#l_image = np.asarray(download_image(image_url)) # face image
#l_image_1 = l_image.copy()


# to add image on the top of image
def add_image(license,photo):
    alpha = 0
    photo = resize(photo ,"photo")
    added_image = cv2.addWeighted(license[83:194,281:392,:], alpha, photo[0:111, 0:111,:], 1 - alpha, 0)
    print(type(added_image))

    license[83:194,281:392, :] = added_image
    return license

# to add text on image
def add_text(license,text, location ,thickness = 2,font = cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5):
    image = cv2.putText(resize(license,"license"), text, location, font,
                        fontScale, color, thickness, cv2.LINE_AA)
    return image

"""

for i in range(0,10):
    
    l = add_text(license=temp_1, text=fake.name(), location=name_l, thickness=1)
    l = add_text(license=l, text=fake.street_address(), location=address_l, thickness=1)
    l = add_text(license=l, text=fake.city() + " VIC " + ranien(), location=address_l2, thickness=1)
    l = add_text(license=l, text=fake.date(), location=dob, thickness=2)
    l = add_text(license=l, text=fake.date(), location=license_exp, thickness=2)
    l = add_text(license=l, text=rangen(), location=license_num, thickness=1, fontScale=0.4)
    l = add_text(license=l, text=random.choice(my_list), location=license_type, thickness=1)
    l = add_text(license=l, text=random.choice(my_con), location=condition, thickness=1)
    l = add_image(photo=l_image_1, license=l)
"""



for i in range(0,10):
    l = add_text(license=temp_1, text=fake.name(), location=name_l, thickness=1)
    l = add_text(license=l, text=fake.street_address(), location=address_l, thickness=1)
    l = add_text(license=l, text=fake.city() + " VIC " + ranien(), location=address_l2, thickness=1)
    l = add_text(license=l, text=fake.date(), location=dob, thickness=2)
    l = add_text(license=l, text=fake.date(), location=license_exp, thickness=2)
    l = add_text(license=l, text=rangen(), location=license_num, thickness=1, fontScale=0.4)
    l = add_text(license=l, text=random.choice(my_list), location=license_type, thickness=1)
    l = add_text(license=l, text=random.choice(my_con), location=condition, thickness=1)
    l = add_image(photo=np.asarray(download_image(image_url)), license=l)
    plt.imshow(l)
    plt.imsave("fake_license/image_{}.jpg".format(i), l)

print("Ended")












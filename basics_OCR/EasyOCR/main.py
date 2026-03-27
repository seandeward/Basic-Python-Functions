
import easyocr
import cv2
# import numpy as np


#:: FUNCTION FOR GETTING THE AVERAGE CONFIDENCE PERCENTAGE ACCROSS ALL FOUND TEXT FIELDS
def get_average(con_list:list[float]):
  if con_list == []:
    return "[!!!] Confidence list is empty!"
  sum_num = int(0)
  amount = int(0)
  for number in con_list:
    sum_num += int(number * 100)
    amount += int(1)
  return int(sum_num / amount)


#:: FUNCTION THAT DETAILS THE PRE-PROCESSING SETTINGS
def preprocess_image(path:str):
  img = cv2.imread(path)

  #* 1. convert to grayscale - removes color noise, most impactful step
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  #* 2. denoise - helps with scanned or photographed images
  # img = cv2.fastNlMeansDenoising(img, h=30)

  #* 4. Increase contrast with CLAHE — evens out uneven lighting
  # clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
  # img = clahe.apply(img)

  return img


#:: INITIALIZE READER
reader = easyocr.Reader(['en'], verbose=False)  # initialize once, reuse for multiple images
img = preprocess_image('facesheet.jpg')
result = reader.readtext(img)


#:: BUILD LIST OF CONFIDENCE PERCENTAGES
confidence_list = []
# result is a list of [bounding_box, text, confidence]
for (bbox, text, confidence) in result:
  print(f"[-] {text}  ({confidence:.0%})")
  confidence_list.append(confidence)


#:: RESULTS SECTION
print("")
print("########## RESULTS ##########")
print(f"  AVERAGE CONFIDENCE  = {get_average(confidence_list)}")
print(f"  AVG NAME CONFIDENCE = {get_average(name_confidence_list)}")
print(f"  AMT. NAMES FOUND    = {num_name_found}")
print("")

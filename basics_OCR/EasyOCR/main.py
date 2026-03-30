
print(f"[:] Importing libraries...")
import psutil
import easyocr
import cv2
# import numpy as np

print("[:] Limiting thread count and declaring lowest priority...")
cv2.setNumThreads(2)  # Sets the max thread count allowed to avoid hogging resources.
psutil.Process().nice(psutil.IDLE_PRIORITY_CLASS) # For Windows - 
#psutil.Process().nice(19) # Linux (0-19, higher = lower priority)

print(f"[:] Loading functions...")
#:: FUNCTION FOR GETTING THE AVERAGE CONFIDENCE PERCENTAGE ACROSS ALL FOUND TEXT FIELDS
def get_average(con_list:list[float]):
  if con_list == []:
    return "[!] Confidence list is empty!"
  sum_num = int(0)
  amount = int(0)
  for number in con_list:
    sum_num += int(number * 100)
    amount += int(1)
  return f"{int(sum_num / amount)}%"


#:: FUNCTION THAT DETAILS THE PRE-PROCESSING SETTINGS
def preprocess_image(path:str):
  img = cv2.imread(path)

  #* 1. GRAYSCALE - removes color noise. REQUIRED FOR SCRIPT TO WORK.
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  #* 2. DENOISE - helps with scanned or photographed images.
  img = cv2.fastNlMeansDenoising(img, h=30)

  #* 3. SHARPEN
    #EasyOCR struggles with soft edges. An unsharp mask works well (according to Claude lol)
  # blurred = cv2.GaussianBlur(img, (0,0), 3)
  # img = cv2.addWeighted(img, 1.5, blurred, -0.5, 0)

  #* 4. CONTRAST boost with CLAHE — evens out uneven lighting.
  # clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
  # img = clahe.apply(img)

  #* 5. UPSCALE
  # img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

  return img


#:: INITIALIZE READER
print("[:] Initializing EasyOCR...")
reader = easyocr.Reader(['en'], verbose=False)  # initialize once, reuse for multiple images

img = str("facesheet.jpg")
print(f"[:] Preprocessing '{img}' ...")
result = reader.readtext(preprocess_image(img))


#:: BUILD LIST OF CONFIDENCE PERCENTAGES
print("[:] Building confidence lists...")
confidence_list = []
name_confidence_list = []
num_name_found = int(0)
# result is a list of [bounding_box, text, confidence]
pt_name = ["justus", "ward"] #? this will end up being the variable passed from the PDF
for (bbox, text, confidence) in result:
  if pt_name[0] in text.lower() and pt_name[1] in text.lower():
    print(f"[#] {text}  ({confidence:.0%})")
    name_confidence_list.append(confidence)
    num_name_found += int(1)
  else:
    print(f"[-] {text}  ({confidence:.0%})")
  confidence_list.append(confidence)


#:: RESULTS SECTION
print("")
print("########## RESULTS ##########")
print(f"  AVERAGE CONFIDENCE  = {get_average(confidence_list)}")
print(f"  AVG NAME CONFIDENCE = {get_average(name_confidence_list)}")
print(f"  AMT. NAMES FOUND    = {num_name_found}")
print("")

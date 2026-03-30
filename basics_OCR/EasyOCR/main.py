
#:: LOAD FUNCTIONS

def list_all_of_file_type(file_type:str="None", file_path:str="./") -> list[str]:
  """Returns a list of strings for each requested file type in a directory.
  Args:
      filepath (str): Target directory filepath."""
  result = [f for f in os.listdir(file_path) 
    if os.path.isfile(os.path.join(file_path, f)) and f.endswith(file_type)]
  return result

def preprocess_image(path:str):
  """Pre-processes an image file for later analysis.
  Args:
      path (str): File path of the image to be processed.
  Returns:
      'img': The pre-processed image file."""
  img = cv2.imread(path)
  #* 1. GRAYSCALE - removes color noise. REQUIRED FOR SCRIPT TO WORK.
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  #* 2. DENOISE - helps with scanned or photographed images.
  img = cv2.fastNlMeansDenoising(img, h=30)
  return img

def rotate_img_90deg_clockwise(image_file):
  return cv2.rotate(image_file, cv2.ROTATE_90_CLOCKWISE)

def print_analysis_results(times_name_was_found:int=0, name_confidence_list:list[float]=[], general_confidence_list:list[float]=[]):
  print("")
  print(colored("########## RESULTS ##########", colored="green"))
  print(colored(f"  AVERAGE CONFIDENCE  = {get_average(general_confidence_list)}", color='green'))
  print(colored(f"  AVG NAME CONFIDENCE = {get_average(name_confidence_list)}", color='green'))
  print(colored(f"  AMT. NAMES FOUND    = {times_name_was_found}", color='green'))
  print("")

def get_average(num_list:list[float]) -> str:
  """Gets the average percentage from a list of float numbers.
  Args:
      num_list (list[float]): The numbers to find the average of.
  Returns:
      str: A string that dispalys the average percentage. """
  if num_list == []:
    return "[!] Confidence list is empty!"
  sum_num = int(0)
  amount = int(0)
  for num in num_list:
    sum_num += int(num * 100)
    amount += int(1)
  return f"{int(sum_num / amount)}%"

if __name__ == "__main__":
  #:: IMPORT LIBRARIES
  from termcolor import colored
  print(colored("[-] Importing libraries...", color='yellow'))
  from platform import system
  import os
  import psutil
  import easyocr
  import cv2
  print(colored("    Done", color='green'))

  #:: CONFIGURABLE SETTINGS / GLOBAL VARIABLES
  #* System Settings
  max_cpu_threads_allowed = int(2) # What's the maximum number of CPU cores allowed to be used in this "script?
  windows_task_priority = psutil.IDLE_PRIORITY_CLASS # Only applies to Windows -- What Window's priority level do you want for this task?
  linux_priority = 19 # Only applies to Linux -- (0-19, higher number = lower priority)

  #* Filepaths
  archive_folder_filepath = str("") # where to save copies of combined files to, in the event of a mishap
  combined_file_output_filepath = str("") # where to move the combined versions of documents to


  #! SCRIPT WOULD GET A LIST OF PDFs, AND CREATE A WHILE LOOP TO ITERATE OVER EACH ONE TO FIND A MATCH


  #:: DECLARE TASK PRIORITY
  print(colored("[-] Limiting thread count and declaring lowest priority...", color='yellow'))
  cv2.setNumThreads(int(max_cpu_threads_allowed))  # Sets the max thread count allowed to avoid hogging resources.

  #* Find name of running OS
  system_name = system()
  print(colored(f"[-] {system_name} OS detected", color="cyan"))
  if system_name == "Windows":
    psutil.Process().nice(windows_task_priority) # Only enable if using Windows
  elif system_name == "Linux":
    psutil.Process().nice(linux_priority)

  print(colored("    Done", color='green'))

  #:: INITIALIZE READER
  print(colored("[-] Initializing EasyOCR...", color='yellow'))
  reader = easyocr.Reader(['en'], verbose=False)  # initialize once, reuse for multiple images
  print(colored("    Done", color='green'))

  #! NORMALLY, SCRIPT WOULD ACTIVATE ONCE A PDF IS DROPPED INTO THE TARGET DIRECTORY. FOR TESTING, IT WILL INITIALIZE AUTOMATICALLY.

  pt_name = ["justus", "ward"] #! PT NAME WOULD NORMALLY BE PROCESSED FROM THE SOURCE PDF FIRST
  print(colored(f"[-] Patient Name: {pt_name[0]} {pt_name[1]}", color='green'))

  #:: GET JPG LIST
  print(colored("[-] Getting list of JPGs...", color='yellow'))
  jpg_list = list_all_of_file_type(".jpg")
  print(colored(f"[-] JPG_list = {jpg_list}", color='green'))

  #:: PROCESS AND ANALYZE EACH JPG IN JPG LIST
  for img in jpg_list:
    pass
    preprocessed_image = preprocess_image(img)
    img_rotations = int(0)

    while True:
      if img_rotations > int(0):
        print(f"  [-] Rotations = {img_rotations}")
      print(f"[-] Analyzing '{img}' ...")
      num_name_found = int(0)
      general_confidence_list = []
      name_confidence_list = []
      result = reader.readtext(preprocessed_image)

      #:: LOOK FOR THE NAME IN THE JPG
      for (bbox, text, confidence) in result:
        if pt_name[0].lower() in text.lower() and pt_name[1].lower() in text.lower():
          num_name_found += int(1)
          name_confidence_list.append(confidence)
        else:
          general_confidence_list.append(confidence)
      
      if num_name_found > int(0):
        print_analysis_results(num_name_found, name_confidence_list, general_confidence_list) 
        #! This will later become where the PDF conversion, appending, and file move will take place.
        break
      elif img_rotations >= int(3):
        print(colored(f"[!] image has already been rotated more than 3 times. Moving on to the next image...", color='red'))
        print('') # for terminal space
        break
      elif num_name_found == int(0):
        print(colored("[!] No matching names found. Rotating image by 90 degrees...", color='yellow'))
        preprocessed_image = rotate_img_90deg_clockwise(preprocessed_image)
        img_rotations += int(1)
      else:
        print(colored(f"[!] There was an error processing the 'num_name_found variable', which equals {num_name_found}", color='red'))
        break

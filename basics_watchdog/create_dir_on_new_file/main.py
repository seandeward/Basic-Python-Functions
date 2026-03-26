
#:: This script watches over the entire Basic-Python-Functions directory and reports any changes to the file system.

#! This script does not work at this time. When a new file is drop into the directory that the script runs from, it continues to make several directories, one after another. This is unintended; The script should only make a single directory for the new file.

import time
import os
import shutil

from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer

# from make_directory import *
from get_time import *

print("[=] STARTING WATCHDOG EVENT HANDLER")

class MyEventHandler(FileSystemEventHandler):
  def on_any_event(self, event: FileSystemEvent) -> None:
    print(f"  [-] New event: {event}")
    
    if event.event_type == 'created' and event.is_directory == False:
      new_file = str(event.src_path)
      print(f"[=] The new file is '{new_file}")
      dir_name = str(get_time())
      if str(dir_name) not in str(event.src_path):
        #:: CREATE THE DIRECTORY
        try:
          os.mkdir(dir_name)
          print(f"[=] Directory {dir_name} created.")
        except FileExistsError:
          print(f"[!] Directory {dir_name} already exists.")
        except PermissionError:
          print(f"[!] Permission Denied: Unable to create {dir_name}.")
        except Exception as e:
          print(f"[!] An error occurred: {e}")

        #:: MOVE NEW FILE TO DIRECTORY
        try:
          shutil.move(new_file, dir_name)
        except Exception as e:
          print(f"[!] An error occurred: {e}")

        time.sleep(2) #? Here only for troubleshooting while the script keeps accidentally making more than one directory. This stops it from making a thousand in seconds.

event_handler = MyEventHandler()
observer = Observer()
observer.schedule(event_handler, ".", recursive=True)
observer.start()
try:
  while True:
    time.sleep(1)
finally:
  observer.stop()
  observer.join()

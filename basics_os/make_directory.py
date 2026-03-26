
def make_directory(dir_name:str):
  import os
  """Creates a directory.

  Args:
      dir_name (str): The new directory's filepath as a string.
  """
  #:: Create the directory
  try:
    os.mkdir(dir_name)
    print(f"[=] Directory {dir_name} created.")
  except FileExistsError:
    print(f"[!] Directory {dir_name} already exists.")
  except PermissionError:
    print(f"[!] Permission Denied: Unable to create {dir_name}.")
  except Exception as e:
    print(f"[!] An error occurred: {e}")

if __name__ == "__main__":
  path = "./basics_os/new_dir"
  make_directory(path)

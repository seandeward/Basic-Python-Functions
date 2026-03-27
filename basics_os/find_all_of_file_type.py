
def list_all_of_file_type(filepath:str, filetype:str) -> list[str]:
  """Returns a list of strings for each requested file type in a directory.

  Args:
      filepath (str): Target directory filepath.
  """
  pdf_files = [f for f in os.listdir(filepath) 
    if os.path.isfile(os.path.join(filepath, f)) and f.endswith(filetype)]
  return pdf_files

if __name__ == "__main__":
  import os
  print(f"PDFs = {list_all_of_file_type(".", ".pdf")}")
  print(f"JPGs = {list_all_of_file_type(".", ".jpg")}")

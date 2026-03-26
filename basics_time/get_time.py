
import time

def get_time():
  return int(round(time.time() * 1000))

if __name__ == "__main__":
  i = int(0)
  while i < 9:
    print(get_time())
    i += 1

import os
import platform
import time

os.system("pip install requests curl_cffi openpyxl")  # প্রয়োজনীয় লাইব্রেরি ইনস্টল করার জন্য
fuck = platform.architecture()[0]

if fuck == "64bit":
  os.system("git pull")
  os.system("clear")
  print("[•] YOUR DEVICE IS 64 BIT")
  time.sleep(2)
  # এখানে আপনার .so ফাইলের নামের প্রথম অংশ লিখতে হবে। 
  # যদি ফাইলটি ff.cpython-...so হয়, তবে লিখবেন: from ff import ff
  from ff import ff

  ff()
elif fuck == "32bit":
  os.system("git pull")
  os.system("clear")
  print("[•] YOUR DEVICE IS 32 BIT")
  time.sleep(2)
  from ff import ff

  ff()
else:
  os.system("clear")
  print("\x1b[1;97m Soon Your Device Supported Tools ")

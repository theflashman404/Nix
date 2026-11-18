import os
import platform
import sys


# আপনার যদি get_number_file_path বা main_menu অন্য ফাইলের হয়, তবে সেগুলো এখানে ডিফাইন বা ইমপোর্ট করতে হবে
def ff():
  try:
    if not os.path.exists("Number_List.txt"):
      with open("Number_List.txt", "w") as f:
        pass
    if not os.path.exists("Proxy_List.txt"):
      with open("Proxy_List.txt", "w") as f:
        pass

    # main_menu()  # আপনার আসল মেনু ফাংশন এখানে কল হবে
    print("Tool is working perfectly!")
  except Exception as e:
    import traceback

    print(f"\nCRITICAL ERROR: {e}")
    traceback.print_exc()
    input("\nPress Enter to exit...")

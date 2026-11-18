import os
import platform
import sys

# যদি আপনার main_menu বা অন্যান্য ফাংশন থাকে সেগুলো এখানে থাকবে বা ইমপোর্ট করা থাকবে
# from module_name import main_menu, get_number_file_path, get_proxy_file_path


def ff():
  try:
    if (
        get_number_file_path() == "Number_List.txt"
        and not os.path.exists("Number_List.txt")
    ):
      with open("Number_List.txt", "w") as f:
        pass
    if get_proxy_file_path() == "Proxy_List.txt" and not os.path.exists(
        "Proxy_List.txt"
    ):
      with open("Proxy_List.txt", "w") as f:
        pass
    main_menu()
  except Exception as e:
    import traceback

    print(f"\nCRITICAL ERROR: {e}")
    traceback.print_exc()
    input("\nPress Enter to exit...")

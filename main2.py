import os
if os.path.exists("JKV.txt"):
    os.remove("JKV.txt")
else:
    print("the file does not exist")
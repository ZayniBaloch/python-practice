import os
if (not os.path.exists("module_sandbox")):
    os.mkdir("module_sandbox")

print(os.getcwd()) # its return the directory we are in #


isAvailable="readme.md"
if os.path.exists(isAvailable):
    print(f"the file '{isAvailable}' exist")
else:
    print("the file doesnt exist")
## ok if you you are not using relative path , then we have to carefully chnage directory because of we are using absolute path , python will try to find that file in new folder but it does'nt exist there so will give wrong results##



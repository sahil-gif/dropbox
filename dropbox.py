
import os 
path = "/home"
print(os.path.join(path, "User/Desktop", "file.txt")) 
path = "User/Documents"
print(os.path.join(path, "/home", "file.txt")) 
path = "/User"
print(os.path.join(path, "Downloads", "file.txt", "/home")) 
path = "/home"
print(os.path.join(path, "User/Public/", "Documents", "")) 



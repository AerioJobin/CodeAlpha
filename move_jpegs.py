import os
import shutil

# Set your source and destination folder paths
source_folder = "C:/Users/YourName/Downloads"       # Change this to your source path
destination_folder = "C:/Users/YourName/Downloads/JPEG_Files"  # Change this to your destination

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Move all .jpeg files
moved_files = 0
for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpeg"):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)
        moved_files += 1
        print(f"Moved: {filename}")

print(f"\nTotal .jpeg files moved: {moved_files}")

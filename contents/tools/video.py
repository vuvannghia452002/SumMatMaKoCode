import os
import glob


root = r"../../"
mp4_files = glob.glob(os.path.join(root, "**/*.mp4"), recursive=True)
for i in mp4_files:
    print("🚀 Giá trị của i:", i)

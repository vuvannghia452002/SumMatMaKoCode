import os
import glob


root = r"../../"
pdf_files = glob.glob(os.path.join(root, "**/*.pdf"), recursive=True)
for i in pdf_files:
    print("🚀 Giá trị của i:", i)

from modules.Convert import Convert
import os
import shutil
import pyperclip
# nhận văn bản
input = pyperclip.paste()
output = Convert.VarSnakeCase(input)
# sao chép file
ten_file_nguon = r"C:\Users\vvn20206205\Desktop\LatexATS\document\latex\contents\a.tex"
ten_file_dich = os.path.join(os.path.dirname(
    ten_file_nguon), f"{output}"+".tex")
shutil.copy(ten_file_nguon, ten_file_dich)
# return văn bản
output = "\\input{contents/" + output + "}"
pyperclip.copy(output)

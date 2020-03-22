import re

JPEG_SOF = b'\xFF\xD8\xFF\xE0'
JPEG_EOF = b'\xFF\xD9'

f = open(r'C:\Users\billy\Desktop\test.docx','rb')
data = f.read()
f.close()

SOF_list = [match.start() for match in re.finditer(re.escape(JPEG_SOF), data)]
EOF_list = [match.start() for match in re.finditer(re.escape(JPEG_EOF), data)]


subdata = data[SOF_list[0]:EOF_list[0]+2]
carve_obj = open('carved_image.jpg' ,'wb')
carve_obj.write(subdata)
carve_obj.close()
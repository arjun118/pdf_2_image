from pdf2image import convert_from_path

import tempfile,os

parent_dir=os.getcwd()
out_dir="extracted_images"
absolute_output_path=os.path.join(parent_dir,out_dir)
os.mkdir(absolute_output_path)

'''
TO-DO

-- MAJOR: make it compatible for both windows and linux

1. take input from the user for the output directory name
2. take the input for the bin dir of poppler
3. check if the input poppler path exists
4. ask the user about the dpi and (if possible )the size of the image they want
5. use threading to speedup the process if possible
6. develop the application with flask

'''    

with tempfile.TemporaryDirectory() as path:
    images_from_path=convert_from_path("test.pdf",output_folder=path,poppler_path="path to poppler bin dir after its installation on windows")
    for i in range(len(images_from_path)):
        fname=os.path.join(absolute_output_path,f'page_{i}.png')
        images_from_path[i].save(fname,'PNG')
    images_from_path=[]
print(images_from_path)

import sys, fitz,os,time
from concurrent.futures import ThreadPoolExecutor
def convert_page_to_image(page):
    pix = page.get_pixmap(dpi=300)  
    pix.save(os.path.join(output_file_dir,f'page_{page.number}.png'))
    return 1
    
def main():
    banner='''
        1. install pymupdf python module using 'pip install pymupdf' or refer to the documentation (https://pymupdf.readthedocs.io/en/latest/installation.html)
        
        USAGE:
        
        python "path_to_the_pdf_file" "name_of_the_output_directory"
    '''
    if len(sys.argv)==2 and sys.argv[1]=='-h' :
        print(banner)
        sys.exit(0)
    if len(sys.argv)!=3:
        msg='''
        Less number of arguments than needed
        run 'python script.py -h' for usage details
        '''
        print(msg)
        sys.exit(1)
    input_file_path=sys.argv[1]
    ## file checks to be implemented
    global output_file_dir
    output_file_dir=sys.argv[2]
    ## find a way to not use global yet getting the job done
    if os.path.exists(os.path.join(os.getcwd(),output_file_dir)):
        msg=f'''
        The directory named {output_file_dir} already exists in your current working directory.
        Try giving a different directory name 
        '''
        print(msg)
        sys.exit(1) 
    doc = fitz.open(input_file_path)
    start=time.perf_counter()
    os.mkdir(output_file_dir)
    with ThreadPoolExecutor() as executor:
        executor.map(convert_page_to_image,doc)
    # for page in doc:
    #     pix = page.get_pixmap(dpi=300)  
    #     pix.save(os.path.join(output_file_dir,f'page_{page.number}.png'))
    end=time.perf_counter()
    print(f"Done, took {end-start} seconds")
    
if __name__=='__main__':
    main()
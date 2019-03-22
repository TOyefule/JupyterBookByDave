# loop through a collection of notebooks and md files
# Tkinter is the easiest way to open a file dialog box 
# if you don't want to have any other dependencies.
import os
import pdfkit # requires https://wkhtmltopdf.org/downloads.html
import tkinter as tk
from tkinter import filedialog

# set properties for the directory open dialog box
root = tk.Tk()
root.wm_attributes('-topmost', 1)
root.lift()
root.withdraw()

# for OSX
# self.root.lift()
# self.root.call('wm', 'attributes', '.', '-topmost', True)
# self.root.after_idle(self.root.call, 'wm', 'attributes', '.', '-topmost', False)

# create TOC (use directory structure and filenames)
def appendTOC(TOC,level,text):
    fh=open(TOC, "a")
    if level == 0:
        fh.write("{0}\n".format(text))
    if level == 1:
        fh.write("\t{0}\n".format(text))
    if level == 2:
        fh.write("\t\t{0}\n".format(text))
    fh.close()
    
print("Select the Directory containing Jupyter Notebooks you wish to convert")
path = filedialog.askdirectory()

for root, directories, filenames in os.walk(path):
    TOC = os.path.join(root,"TableOfContents")
    
    if os.path.isfile(TOC):
        os.unlink(TOC)
    appendTOC(TOC,0,root)
    
    #for directory in directories:
    for filename in filenames:
        name, ext = os.path.splitext(filename)
        infile = os.path.join(root,filename)
        if ext == ".html":
            os.unlink(infile)
        else:
            outfile = os.path.join(root,filename)
            outfile += ".html"
            # print(outfile)
        
# TODO: Replace os.system with subprocess:
# https://stackoverflow.com/questions/4813238/difference-between-subprocess-popen-and-os-system
            if filename.endswith("ipynb"):    
                cmd = "jupyter nbconvert --output \"{0}\" --to html --template basic \"{1}\"".format(outfile,infile)
                # print (cmd)
                os.system(cmd)                
                # add filename to TOC
                # print("TOC: {0} {1}",TOC,filename)
                appendTOC(TOC,0,filename)
            
            if filename.endswith("md"):
                cmd = "grip \"{0}\" --export \"{1}\"".format(infile,outfile)
                # print (cmd)
                os.system(cmd)
                # add filename to TOC
                # print("TOC: {0} {1}",TOC,filename)
                appendTOC(TOC,0,filename)
            
print ("done converting .ipynb and .md to .html")

#create PDFs
# TODO: fix images - they don't show.
# TODO: Is wkhtmltopdf in the path?
# TODO: prompt to find file
path_wkthmltopdf = r'C:\Users\GBTC440001ur\djw\jupyterbook\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)

for root, directories, filenames in os.walk(path):
    for filename in filenames:
        name, ext = os.path.splitext(filename)
        infile = os.path.join(root,filename)
        print(infile)
        if ext == ".html":  
            outfile = os.path.join(path,filename + ".pdf")
            print(outfile)
            pdfkit.from_file(infile,outfile,configuration=config)

print ("done making PDFs")

# push to github


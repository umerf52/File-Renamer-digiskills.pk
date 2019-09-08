File renaming script for Digiskills.pk Freelancing course

Recommended way to structure the files is:   
Root   
|_ Week 1   
|_ Week 2   
|_ ...   

# Logic
Script starts by checking if there are `.mkv` and `.description` files of the same name in the `Root` folder. If these files are found, it reads the title of the video from the `.description` and renames the `.mkv` file.   
Once the script has processed the `Root` folder completely, it recursively starts processing sub-folders.

# Environment
Python 3.7.4   
Windows 10 Version 10.0.18362.295

### Note
This script was tested only on Freelancing course. This may or may not work on other courses.
# python2image
This is quite a silly program (as it doesnt really do anythin) but it is an easier way to send code files to people (some apps dont let you send .py files)
This app reads the contents of the python file, then converts the characters into colours, adds them to an image file and then saves it (with the same name as the python file)
This can be reversed as well, with all the pixels read and the characters put back into their respective place (with necessary linebreaks, \n, etc)

## Usage
Upon starting, the program will ask for 'File name with extension' -> including the extension is VERY IMPORTANT <br>
If the extension is .py it will convert to .png; else if the extension is .png it will convert to .py

## Python 2 Img (CodeLike)
This version of the code converts it into an image, but keeps the linebreaks similar to the code:
![test.py](https://github.com/OGD311/python2image/assets/114223604/686403e0-30da-4f0c-9d51-cabe76b42c12) <br>
Gets converted to: <br>
![testCodelike.png](https://github.com/OGD311/python2image/assets/114223604/3867fe23-265d-4acd-828d-58e1ca268361)


## Python 2 Img (Square)
This version of the code converts it into an image, but makes the image square (much nicer to look at and overall a smaller image):
![test.py](https://github.com/OGD311/python2image/assets/114223604/686403e0-30da-4f0c-9d51-cabe76b42c12) <br>
Gets converted to: <br>
![testSquare.png](https://github.com/OGD311/python2image/assets/114223604/f2e2fbe0-bd62-44dc-903a-4f2b66949bfc)

from PIL import Image
import math

# Colours per character
ascii_colors = {chr(i): (i % 256, (i * 2) % 256, (i * 3) % 256) for i in range(128)}
ascii_colors['\n'] = (255, 165, 0)  # Set color for newline character (orange)

def readFile(fileName):
    newlines = ''
    with open(fileName, 'r') as file:
        content = file.readlines()

    for line in content:
        newlines += line 

    return newlines

def createImg(lines):
    size = (math.ceil(math.sqrt(len(lines))), math.ceil(math.sqrt(len(lines))))

    img = Image.new(mode="RGB", size=size)
    return img

def addChrs(img, content):
    x, y = 0, 0
    for line in content:
        for char in line:
            img.putpixel((x, y), ascii_colors.get(char, (255, 255, 255)))
            x += 1
            if x == img.size[0]:
                y += 1
                x = 0
    return img


def saveImg(img, output_filename):
    img.save(output_filename)


def readChrs(img, file):
    width, height = img.size
    fileName = file.replace('.png', '.py')
    with open(fileName, 'w') as file:
        indentation = 0
        line = ''
        for y in range(height):
            for x in range(width):
                curPixel = img.getpixel((x, y))
                char = next((ch for ch, rgb in ascii_colors.items() if rgb == curPixel), None)
                line += char if char and char != '\x00' else ' '  # Replace NUL character with space
                if char == '\n':
                    file.write(' ' * indentation + line.rstrip() + '\n')
                    line = ''  # Reset line for the next line in the image
                    indentation = 0  # Reset indentation for the next line
                if x == width - 1 and y == height - 1:
                    file.write(' ' * indentation + line.rstrip())  # Write the last line with proper indentation


while True:
    file = input("Enter the file name with extension: ")
    if '.py' in file:
        print('Converting to image...')
        content = readFile(file)
        img = addChrs(createImg(content), content)
        img = img.crop(img.getbbox())  # Squish image
        saveImg(img, file.replace('.py', '.png'))
        print(f"Image '{file.replace('.py', '.png')}' created successfully!")

    elif '.png' in file:
        print('Converting to python...')
        img = Image.open(file)
        readChrs(img, file)
        print(f"Text extracted and saved to '{file.replace('.png', '.py')}'")

    else:
        print('Invalid option. Please enter 1 or 2.')

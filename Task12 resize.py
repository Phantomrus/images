import PIL
import sys
import argparse
import os


def createParser():
    parser = argparse.ArgumentParser(description="Изменение размера изображения",)
    parser.add_argument ('path',  nargs='?',
    		help="Путь к исходному изображению.")
    parser.add_argument ('-w', '--width', nargs='?', 
    		help="Ширина результирующего изображения.")
    parser.add_argument ('-h', '--height', nargs='?',
    		help="Высота результирующего изображения.")
    parser.add_argument ('-s', '--scale', nargs='?',
    		help="Масштаб, который следует использовать при изменении размера изображения.")
    parser.add_argument ('-o', '--output' nargs='?', 
    		help="Директория, в которую требуется сохранить результирующее изображение.")
  
    return parser
 
def analyze_arguments():


def check_for_errors():



def open_image(path_to_original_image): 
	if os.path.exists(path_to_file):
		image = Image.open("path_to_original_image")
		return image
	else:
		print("Указанный файл не найден")


def resize_image(path_to_original_image, path_to_result, width=None, height=None, scale=None):
    pass



if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
 
    print (namespace)

    if namespace.name:
        print ("Привет, {}!".format (namespace.name) )
    else:
        print ("Привет, мир!")
    path_to_original_image = 
    width_new = 

    image = open_image(path_to_original_image)
    name = path_to_original_image.rfind('\\',0,len(s))[a+1:]
	filename_extension = namr.rfind('.',0,len(s))[a+1:]
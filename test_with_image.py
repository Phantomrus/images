import random
from PIL import Image, ImageDraw  

if __name__ == '__main__':
	
	mode = int(input("Please, choose mode:\n",
				"0 - gray\n",
				"1 - sepia\n",
				"2 - negative\n",
				"3 - noise\n",
				"4 - brightness\n",
				"5 - bw"))

	image = Image.open("temp.jpg")
	draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 

	width = image.size[0]  
	height = image.size[1]  	
	pix = image.load() #Выгружаем значения пикселей.
	
	if (mode == 0):
		for i in range(width):
			for j in range(height):
				a = pix[i, j][0] * 0.2126 #0.30
				b = pix[i, j][1] * 0.7152 #0.59
				c = pix[i, j][2] * 0.0722 #0.11
				
				draw.point((i, j), (S, S, S))

	if (mode == 1):
		depth_of_sepia = int(input('depth of sepia:'))
		for i in range(width):
			for j in range(height):
				a, b, c = pix[i, j]

				S = (a + b + c) // 3
				a = S + depth * 2
				b = S + depth
				c = S

				a,b,с = [min(i,255) for i in (a,b,c)]

				draw.point((i, j), (a, b, c))

	if (mode == 2):
		for i in range(width):
			for j in range(height):
				a, b, c = pix[i, j]

				draw.point((i, j), (255 - a, 255 - b, 255 - c))

	if (mode == 3):
		factor = int(input('factor:'))
		for i in range(width):
			for j in range(height):
				rand = random.randint(-factor, factor)
				a = pix[i, j][0] + rand
				b = pix[i, j][1] + rand
				c = pix[i, j][2] + rand
				
				a,b,с = [max(i,0) for i in (a,b,c)]
				a,b,с = [min(i,255) for i in (a,b,c)]

				draw.point((i, j), (a, b, c))

	if (mode == 4):
		factor = int(input('factor:'))
		for i in range(width):
			for j in range(height):
				a = pix[i, j][0] + factor
				b = pix[i, j][1] + factor
				c = pix[i, j][2] + factor

				a,b,с = [max(i,0) for i in (a,b,c)]
				a,b,с = [min(i,255) for i in (a,b,c)]

				draw.point((i, j), (a, b, c))

	if (mode == 5):
		factor = int(input('factor:'))
		for i in range(width):
			for j in range(height):

				a, b, c = pix[i, j]
				
				middle = (a + b + c) / 3

				a, b, c = [255 if middle > (255 + factor) // 2 else 0 for i in (a, b, c)]
	
				draw.point((i, j), (a, b, c))

	image.save("ans.jpg", "JPEG")

	del draw
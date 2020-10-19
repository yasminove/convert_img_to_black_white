from PIL import Image

baby = Image.open('baby.jpeg')

black_white = baby.convert('L')

black_white.show()
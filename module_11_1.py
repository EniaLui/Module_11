from PIL import Image
#Pillow — улучшенная версия библиотеки PIL, в коде импорта она называется PIL.

# библиотека Pillow позволяет работу с изображениями.
#Image.open() - открывает картинку. .save() - сохраняет картинку; .show() - показывает картинку


#Атрибуты картинок в  Pillow:
#format — формат данных картинки: jpeg, png
#mode — цветовая модель картинки: CMYK, RGB, L — для чёрно-белых изображений.
#width — ширина картинки в пикселях.
#height — высота картинки в пикселях.
#size — размер картинки в пикселях. Возвращает tuple: (ширина, высота).

#функция для вывода атрибутов картинки
def attribute_image(img):
    image = Image.open(img)
    print(image.format)
    print(image.mode)
    print(image.width)
    print(image.height)
    print(image.size)

# Функция вращения на определенный градус
def rotated_image (img, degree):
    image = Image.open(img)
    rotated_image = image.rotate(degree)
    rotated_image.save(f'rotated{img}.jpg')

# Метод .transpose() для преобразований, в качестве аргументов можно передать:
# Image.FLIP_LEFT_RIGHT: зеркальное отображение.
# Image.FLIP_TOP_BOTTOM: переворачивает  сверху вниз.
# Image.ROTATE_90: поворачивает на 90 градусов против часовой стрелки.
# Image.ROTATE_180: поворачивает на 180 градусов.
# Image.ROTATE_270: поворачивается на 270 градусов против часовой стрелки/90 градусов по часовой стрелке.
# Image.TRANSPOSE: перемещает строки и столбцы, используя верхний левый пиксель в качестве источника, при этом верхний левый пиксель в перемещенном изображении такой же, как и в исходном изображении.
# Image.TRANSVERSE: перемещает строки и столбцы, используя нижний левый пиксель в качестве источника, при этом нижний левый пиксель остается фиксированным относительно исходной и измененной версиями.

#Функция перевода в другую цветовую модель
def change_mode(img, mode):
    image = Image.open(img)
    change_image = image.convert(mode)
    change_image.save(f'change_mode{img}.jpg')

#Функция обрезания картинки. Метод .crop() принимает кортеж из 4 чисел: координаты углов новой картинки:
# отсчитываются с левого верхнего угла картинки: слева, сверху, справа, снизу.

def crop_image(img, size: tuple):
    image = Image.open(img)
    cropped = image.crop(size)
    cropped.save(f'crop_image{img}.jpg')

# Библиотека позволяет уменьшать размера картинки не сохраня пропорции: (resize)
# И сохраняя пропорции: thumbnail

#Разделить Картинку на цветовые каналы: split, собрать из картинок разных цветовых каналов:Image.merge(mode, tuple за каналов)
# И перекрасить цветовые каналы: ImageOps.colorize(image, black ="цвет", white ="цвет")
# Наложение картинок друг на друга Image.blend(image1, image2, коофицент прозрачности: float)

# Метод filter() - ползволяет огромное количество манипуляций, например:
# Размытие картинок: img.filter(ImageFilter.BLUR(число)/ImageFilter.GaussianBlur(20))
# Резкость картинок: img.filter(ImageFilter.SHARPEN)
# Границы обЬекта на картинке:
#img_wb = img.convert("L") - переводим в черно белое
#edges = img_wb.filter(ImageFilter.FIND_EDGES) - определяем границы

#Библиотека позволяет вырезать части изображения и создавать коллажи
#Функция наложения водяного знака
def logo(img, logo, place: tuple): #изображение куда вставлять, водяной знак, место положения водяного знака: координаты верхний левый угол изображения
    with Image.open(logo) as img_logo:
        img_logo.load()
    with Image.open(img) as img_img:
        img_img.load()
    img_img.paste(img_logo, (place), img_logo)
    img_img.save(f'logo{img}.jpg')

#библиотека позволяет сравнивать ихзображения, создавать изображения, создавать анимацию




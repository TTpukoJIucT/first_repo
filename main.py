import torch
from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt


# Декодинг jpeg
def decode_jpeg(file_path):
    with open(file_path, 'rb') as f:
        img = Image.open(f)
    return img


# Енкодинг jpeg с заданным качеством (quality от 1 до 95)
def encode_jpeg(img, quality=95):
    img.save('encoded_image.jpg', format='JPEG', quality=quality)


# Ресайз изображения
def resize_image(img, size):
    transform = transforms.Compose([transforms.Resize(size)])
    return transform(img)


# Кроп изображения
def crop_image(img, top_left, bottom_right):
    return transforms.functional.crop(img, top_left[1], top_left[0], bottom_right[1] - top_left[1],
                                      bottom_right[0] - top_left[0])


# Поворот изображения (угол в градусах)
def rotate_image(img, angle):
    transform = transforms.Compose([transforms.functional.rotate(img, angle)])
    return transform(img)


# Пример использования функций
if __name__ == '__main__':
    # Укажите путь к вашей исходной картинке
    image_path = 'path_to_your_image.jpg'

    # Загрузка изображения
    image = decode_jpeg(image_path)

    # Оригинальное изображение
    plt.figure()
    plt.title("Original Image")
    plt.imshow(image)
    plt.axis('off')
    plt.show()

    # Ресайз изображения
    new_size = (200, 200)
    resized_image = resize_image(image, new_size)

    # Вывод ресайзнутого изображения
    plt.figure()
    plt.title("Resized Image")
    plt.imshow(resized_image)
    plt.axis('off')
    plt.show()

    # Кроп изображения
    top_left = (50, 50)
    bottom_right = (150, 150)
    cropped_image = crop_image(image, top_left, bottom_right)

    # Вывод кропнутого изображения
    plt.figure()
    plt.title("Cropped Image")
    plt.imshow(cropped_image)
    plt.axis('off')
    plt.show()

    # Поворот изображения
    angle_degrees = 45
    rotated_image = rotate_image(image, angle_degrees)

    # Вывод повернутого изображения
    plt.figure()
    plt.title("Rotated Image")
    plt.imshow(rotated_image)
    plt.axis('off')
    plt.show()

    # Енкодинг jpeg с заданным качеством
    encode_jpeg(rotated_image, quality=80)

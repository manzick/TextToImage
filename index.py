#
# index.py
# Заголовочный файл
#
# by Manzick

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import config

IMAGE_NAME = config.IMAGE_NAME
FONT_SIZE = config.FONT_SIZE
FONT_NAME = config.FONT_NAME
FILE_LINES = config.FILE_LINES
FIRST_NUMBER = config.FIRST_NUMBER
SPACE_SIZE = config.SPACE_SIZE
TOP_SPACE = config.TOP_SPACE
LEFT_SPACE = config.LEFT_SPACE
CHAR_MAX = config.CHAR_MAX


def draw_to_image(texts, output_name):
    """
    Функция пишет текст на картинке base.jpg
    :text: текст, который будет записан в картинку
    :output_name: название выходного файла
    """
    font = ImageFont.truetype(FONT_NAME, FONT_SIZE)
    image = Image.open(IMAGE_NAME)

    global TOP_SPACE
    top_space_local = TOP_SPACE
    if len(texts) > 2:
        top_space_local = TOP_SPACE - (len(texts) - 2) * 15
    line_number = 1
    for text in texts:
        y_position = (top_space_local - SPACE_SIZE) + line_number * SPACE_SIZE
        text_position = (LEFT_SPACE, y_position)
        text_color = (255, 255, 255)

        draw = ImageDraw.Draw(image)
        draw.text(text_position, text, text_color, font)
        line_number = line_number + 1

    address = os.path.abspath(os.curdir)
    image.save(address + '/output/' + output_name + '.png')


def get_lines(file_name):
    """
    Достает строки из файла с именем
    :file_name: имя файла из которого берутся строки
    :return: Массив строк
    """
    lines = []
    f = open(file_name)
    line = f.readline()
    while line:
        lines.append(line)
        line = f.readline()
    f.close()
    return lines


def get_list_in_string(line):
    """
    Получает текст, и если он длинее определенного количества символов разбивает его на список строк
    :param line: текст
    :return: список строк
    """
    list = []
    while len(line) > CHAR_MAX:
        number_char = CHAR_MAX - 1
        while line[number_char] != ' ' and (number_char + 1) < len(line):
            number_char = number_char - 1
        temp_string = line[:number_char]
        if temp_string[0] == ' ':
            temp_string = temp_string[1:]
        list.append(temp_string)
        line = line[number_char:]
    if line[0] == ' ':
        line = line[1:]
    list.append(line)
    return list


def main():
    lines = get_lines(FILE_LINES)
    now_number = FIRST_NUMBER
    print('На первый взгляд, Вы указали параметры верно! Тогда начинаем:')
    for line in lines:
        texts = get_list_in_string(line)
        now_number = now_number + 1
        number = str(now_number)
        draw_to_image(texts, number)
    print(str(now_number) + ' изображений было создано')
    print('Хорошая работа!')


if __name__ == "__main__":
    main()

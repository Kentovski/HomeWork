# /usr/bin/python3

# MELNIKOV ILYA

import turtle
import collections
import random

RADIUS = 100
LENGTH = 50
START_COORD = [-150, -100]
CENTER_COORD = [-150, 0]


def draw_label(turt_arrow, word_counter, coord_top_label, key):
    turt_arrow.goto(coord_top_label)
    turt_arrow.down()
    turt_arrow.dot(10)
    turt_arrow.up()
    turt_arrow.goto(coord_top_label[0] + 50, coord_top_label[1] - 5)
    turt_arrow.write(key + ' - ' + str(word_counter[key]) + ' time(-s)')
    turt_arrow.up()


def draw_diagram(turt_arrow, total_words, word_counter):
    turt_arrow.up()
    turt_arrow.goto(START_COORD)
    turt_arrow.down()

    coord_top_label = [100, 250]  # Координаты лейбла

    for key in word_counter:
        color = (random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255))

        turt_arrow.fillcolor(color)  # Рисуем долю слова
        turt_arrow.pencolor(color)
        turt_arrow.begin_fill()
        turt_arrow.circle(RADIUS, 360 / total_words * word_counter[key])

        pos = turt_arrow.position()  # Запоминаем позицию и направление
        head = turt_arrow.heading()

        turt_arrow.goto(CENTER_COORD)
        turt_arrow.end_fill()
        turt_arrow.up()

        draw_label(turt_arrow, word_counter, coord_top_label, key)  # Пишем надпись
        coord_top_label[1] -= 25

        turt_arrow.goto(pos)
        turt_arrow.seth(head)


def draw_rays(turt_arrow, word_counter):
    turt_arrow.up()
    turt_arrow.goto(START_COORD)
    turt_arrow.down()

    for key in word_counter:
        color = (random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255))
        turt_arrow.pencolor(color)
        head = turt_arrow.heading()

        i = 0
        while i < word_counter[key]:
            turt_arrow.fd(LENGTH)
            turt_arrow.circle(5)
            i += 1

        turt_arrow.up()
        turt_arrow.fd(30)
        turt_arrow.down()
        turt_arrow.write(key)
        turt_arrow.up()
        turt_arrow.goto(START_COORD)
        turt_arrow.seth(head)
        turt_arrow.lt(360/len(word_counter))
        turt_arrow.down()


def draw(text, way):
    win = turtle.Screen()
    win.colormode(255)
    turt_arrow = turtle.Turtle()
    turt_arrow.speed('fastest')

    text = text.lower()
    text_list = text.split()
    total_words = len(text_list)  # Общее количество слов
    word_counter = collections.Counter(text_list)

    if way == 'sectors':
        draw_diagram(turt_arrow, total_words, word_counter)
    else:
        draw_rays(turt_arrow, word_counter)

    win.exitonclick()


def main():
    text = 'hello world hello world nice to meet you'
    # way = 'sectors'
    way = 'rays'

    draw(text, way)

if __name__ == '__main__':
    main()

# /usr/bin/python3

# MELNIKOV ILYA

import turtle


def draw_triangle(turt_arrow, coord_one, coord_two, coord_three, back_color):
    turt_arrow.up()
    turt_arrow.goto(coord_one)
    turt_arrow.down()
    turt_arrow.fillcolor(back_color)
    turt_arrow.begin_fill()
    turt_arrow.goto(coord_two)
    turt_arrow.goto(coord_three)
    turt_arrow.goto(coord_one)
    turt_arrow.end_fill()


def draw_fractal_triangle(turt_arrow, coord_one,
                          coord_two, coord_three, triangle_color, num_iter):
    if num_iter > 0:
        num_iter -= 1

        draw_triangle(turt_arrow,
                      get_middle(coord_one, coord_two),
                      get_middle(coord_two, coord_three),
                      get_middle(coord_three, coord_one),
                      triangle_color)

        draw_fractal_triangle(turt_arrow,
                              coord_one,
                              get_middle(coord_one, coord_two),
                              get_middle(coord_one, coord_three),
                              triangle_color,
                              num_iter)

        draw_fractal_triangle(turt_arrow,
                              get_middle(coord_one, coord_two),
                              coord_two,
                              get_middle(coord_two, coord_three),
                              triangle_color,
                              num_iter)

        draw_fractal_triangle(turt_arrow,
                              get_middle(coord_three, coord_one),
                              get_middle(coord_two, coord_three),
                              coord_three,
                              triangle_color,
                              num_iter)


def get_middle(apex_one, apex_two):
    return [(apex_one[0] + apex_two[0]) / 2, (apex_one[1] + apex_two[1]) / 2]


def main():
    win = turtle.Screen()
    turt_arrow = turtle.Turtle()
    turt_arrow.speed('fast')

    coord_one = [-200, -50]
    coord_two = [0, 250]
    coord_three = [200, -50]

    back_color = 'black'
    triangle_color = 'white'

    num_iter = 6

    draw_triangle(turt_arrow, coord_one, coord_two, coord_three, back_color)
    draw_fractal_triangle(turt_arrow, coord_one, coord_two,
                          coord_three, triangle_color, num_iter)

    win.exitonclick()


if __name__ == '__main__':
    main()

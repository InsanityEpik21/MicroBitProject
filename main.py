def on_button_pressed_a():
    global Playing, Row, Stack
    if Row < 4:
        if Col != Stack:
            Playing = 0
            basic.pause(1000)
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
            """)
            basic.show_icon(IconNames.NO)
        elif Row == 0:
            Playing = 0
            basic.pause(1000)
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
            """)
            basic.show_icon(IconNames.HAPPY)
        else:
            Row += -1
    else:
        Stack = Col
        Row += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Playing, direction, Stack, Col, Row
    Playing = 0
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
    direction = 0
    Stack = 0
    Col = 0
    Row = 4
    Playing = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

direction = 0
Stack = 0
Col = 0
Playing = 0
Row = 0
Row = 4
Playing = 1

def on_forever():
    global Col, direction
    if Playing:
        led.unplot(Col, Row)
        # Going left
        # or
        # Going right
        #
        if direction:
            Col += -1
            if Col == 0:
                direction = 0
        else:
            Col += 1
            if Col == 4:
                direction = 1
        led.plot(Col, Row)
        basic.pause(100)
basic.forever(on_forever)
#Reference Below
#https://makecode.microbit.org/77603-52119-10685-42865
#I got the idea for stacker from the ones at malls and arcades
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (Row < 4) {
        if (Col != Stack) {
            Playing = 0
            basic.pause(1000)
            basic.showLeds(`
                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
            `)
            basic.showIcon(IconNames.No)
        } else if (Row == 0) {
            Playing = 0
            basic.pause(1000)
            basic.showLeds(`
                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
            `)
            basic.showIcon(IconNames.Happy)
        } else {
            Row += -1
        }
        
    } else {
        Stack = Col
        Row += -1
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    Playing = 0
    basic.showLeds(`
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    `)
    direction = 0
    Stack = 0
    Col = 0
    Row = 4
    Playing = 1
})
let direction = 0
let Stack = 0
let Col = 0
let Playing = 0
let Row = 0
Row = 4
Playing = 1
basic.forever(function on_forever() {
    
    if (Playing) {
        led.unplot(Col, Row)
        //  Going left
        //  or
        //  Going right
        // 
        if (direction) {
            Col += -1
            if (Col == 0) {
                direction = 0
            }
            
        } else {
            Col += 1
            if (Col == 4) {
                direction = 1
            }
            
        }
        
        led.plot(Col, Row)
        basic.pause(100)
    }
    
})

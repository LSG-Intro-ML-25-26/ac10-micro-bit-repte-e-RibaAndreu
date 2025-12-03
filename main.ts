let mode = -1
let x = 2
let y = 2
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    mode = 0
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    mode = 1
})
basic.forever(function on_forever() {
    let accX: number;
    let accY: number;
    
    if (mode == 0) {
        led.plotBarGraph(input.temperature(), 50)
    } else if (mode == 1) {
        led.plot(x, y)
        basic.pause(50)
        led.unplot(x, y)
        accX = input.acceleration(Dimension.X)
        accY = input.acceleration(Dimension.Y)
        if (accX <= 150 && x > 0) {
            x -= 1
        }
        
        if (accX > 150 && x < 4) {
            x += 1
        }
        
        if (accY <= 150 && y > 0) {
            y -= 1
        }
        
        if (accY > 150 && y < 4) {
            y += 1
        }
        
    }
    
})

mode = -1  
x = 2
y = 2

def on_button_pressed_a():
    global mode
    mode = 0

def on_button_pressed_b():
    global mode
    mode = 1

input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global x, y, mode

    if mode == 0:
        led.plot_bar_graph(input.temperature(), 50)

    elif mode == 1:
        led.plot(x, y)
        basic.pause(50)
        led.unplot(x, y)

        accX = input.acceleration(Dimension.X)
        accY = input.acceleration(Dimension.Y)

        if accX <= 150 and x > 0:
            x -= 1
        if accX > 150 and x < 4:
            x += 1

        if accY <= 150 and y > 0:
            y -= 1
        if accY > 150 and y < 4:
            y += 1

basic.forever(on_forever)

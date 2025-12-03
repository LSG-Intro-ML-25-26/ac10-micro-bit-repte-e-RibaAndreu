def on_forever():
    led.plot_bar_graph(input.temperature(), 50)
basic.forever(on_forever)

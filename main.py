import pyglet


window = pyglet.window.Window(width=1280, height=960)


@window.event
def on_draw():
    window.clear()


def update(dt):
    pass


pyglet.clock.schedule_interval(update, 1/60.0)  # update at 60Hz


if __name__ == '__main__':
    pyglet.app.run()

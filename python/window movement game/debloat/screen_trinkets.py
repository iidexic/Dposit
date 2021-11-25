from screeninfo import get_monitors

MONITORS = get_monitors()
SCREENW = MONITORS[0].width
SCREENH = MONITORS[0].width

def monitor():
    return (SCREENW, SCREENH)
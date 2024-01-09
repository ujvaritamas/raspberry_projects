import simple_sds011
import time

def configure():
    pm = simple_sds011.SDS011('/dev/ttyUSB0')
    pm.mode = simple_sds011.MODE_PASSIVE
    pm.period

    return pm


def app():
    pm = configure()

    for i in range(1000):
        print(pm.query())
        time.sleep(2)

app()




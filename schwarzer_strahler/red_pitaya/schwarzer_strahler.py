from redpitaya.overlay.mercury import mercury as overlay
import numpy as np
import time
import os

class SchwarzerStrahler:
    def __init__(this, messanzahl:int = 1000):
        this.trig = messanzahl;
        this.fpga = overlay();
        this.osc = this.fpga.osc(0, 20.0)

        this.osc.decimation = 1
        this.osc.trigger_pre = 0
        this.osc.trigger_post = this.trig

        this.osc.trig_src = 0

        this.gpio = this.fpga.gpio
        this.init_pin = this.gpio("n", 0, "out")
        this.ready_pin = this.gpio("n", 1, "in")
        this.step_pin = this.gpio("n", 2, "out")
        this.endswitch_pin = this.gpio("n", 3, "in")

        # init func from script 457
        this.init_pin.write(True)
        start = time.time()
        while this.ready_pin.read() = True:
            if time.time() - start > 1:
                print('Jumped, cause: Time')
                break;
            pass
        while this.ready_pin.read() == False:
            pass
        this.init_pin.write(False)

    def measure(this):
        this.osc.reset()
        this.osc.start()
        this.osc.trigger()
        while this.osc.status_run():
            pass
        return this.osc.data(this.trig)

    def waitForStep(this):
        this.step_pin.write(True)
        start = time.time()
        while this.ready_pin.read() == True:
            if time.time() - start > 1:
                print('Jumped, cause: Time')
                break;
            pass
        while this.ready_pin.read() == False:
            pass
        this.step_pin.write(False)

    def run(this, filename:str, steps:int = 100):
        with open(filename, 'w', encoding='utf-8', buffering=1) as file:
            file.write("Schritt,Messwert,Offset\n")
            
            for i in range(steps):
                if this.endswitch_pin.read() != True:
                    file.write('{},{}\n'.format(i, np.mean(this.measure())))
                    print(f'{100 * i / steps}%', end='\r')
                    this.waitForStep()
                else:
                    print('Reached End\n')
                    break;

from litex.build.generic_platform import *
from litex.build.altera import AlteraPlatform
from litex.build.altera.programmer import USBBlaster

_io = [
        #clk
        ("clk50",0,Pins("E1")),
        # reset
        ("rst_n",0,Pins("M1")),
        #buttons
        ("key",0,Pins("E16")),
        ("key",1,Pins("E15")),
        ("key",2,Pins("M2")),
        ("key",3,Pins("M16")),
        #led
        ("led",0,Pins("D11")),
        ("led",1,Pins("C11")),
        ("led",2,Pins("E10")),
        ("led",3,Pins("F9"))
        ]

class Platform(AlteraPlatform):
    default_clk_name   = "clk50"
    default_clk_period = 1e9/50e6

    def __init__(self, toolchain="quartus"):
        AlteraPlatform.__init__(self, "EP4CE10F17C8", _io, toolchain="quartus")

    def create_programmer(self):
        return USBBlaster()

    def do_finalize(self, fragment):
        AlteraPlatform.do_finalize(self, fragment)
        self.add_period_constraint(self.lookup_request("clk50", loose=True), 1e9/50e6)
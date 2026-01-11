from migen import *
from board import Platform

class Blink(Module):
    def __init__(self,led):
        counter = Signal(max=50000000) #counter full every 1 seconds
        timer4 = Signal(4)
        # synchronous assignments
        self.sync += [
            counter.eq(counter + 1)
        ]
        # combinatorial assignements
        self.sync += If(counter == 0,
            timer4.eq(timer4 + 1)
        )
        self.comb += led.eq(timer4)



class _CRG(Module):
    def __init__(self,platform):
        self.clock_domains.cd_sys = ClockDomain("sys")

        clk50 = platform.request("clk50")
        self.comb += self.cd_sys.clk.eq(clk50)
        board_rst_n = platform.request("rst_n")
        self.comb += self.cd_sys.rst.eq(~board_rst_n)

class Top(Module):
    def __init__(self,platform):
        self.submodules.crg = _CRG(platform)
        self.submodules.blink = Blink(platform.request_all("led"))

if  __name__ == "__main__":
    platform = Platform()
    design = Top(platform)
    platform.build(design)
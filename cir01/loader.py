from board import Platform
import sys

if __name__ == "__main__":
    platform = Platform()
    prog = platform.create_programmer()
    # I guess the params must be file name
    assert(len(sys.argv) == 2 )
    file_name = sys.argv[1]
    print(f"load ${file_name} to FPGA")
    prog.load_bitstream(file_name)

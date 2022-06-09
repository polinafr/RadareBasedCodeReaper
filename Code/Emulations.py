import r2pipe
import Code.FunctionClass

def emulate_function(func, binary):
    r = r2pipe.open(binary)
    addr = "0x"+hex(func.offset)[2:].zfill(8)
    #print(addr)
    s = 's '+addr
    print(s)
    r.cmd(s)
    #r.cmd("s 0x00400400")
    print(r.cmd("pd"))
    #  initialize stack machine for emulation
    r.cmd("aeim")
    print("stack machine created")
    #  working commands: 'ar,' - table view; 'ar' - register and value
    #if show_reg:
    print(r.cmd("ar"))
    print(r.cmd("ad@r:SP"))
    print(r.cmd("ad@r:SP"))
   # print("aeim")
    #registers = r.cmd("aer")
    #print(registers)
    aesu = 'aesu 0x' + hex(func.offset + 6)[2:].zfill(8)
    print(aesu)
    #  emulate from the start of the func until specified address
    r.cmd(aesu)
    #if show_reg:
    print(r.cmd("ar"))
    print(r.cmd("ad@r:SP"))
    print(r.cmd("ad@r:SP"))


def show_env_data(r, show_reg, show_st):
    if show_reg:
        show_registers(r)
    if show_st:
        show_stack(r)


def show_stack(r):
    print("The stack values are:")
    print(r.cmd("ad@r:SP"))


def show_registers(r):
    print("The register values now are:")
    registers = r.cmd("ar,")
    print(registers)



import r2pipe
import Code.FunctionClass


def emulate_function(func, binary):
    r = r2pipe.open(binary)
    addr = "0x"+hex(func.offset)[2:].zfill(8)
    #print(addr)
    s = 's '+addr
    #print(s)
    r.cmd(s)
    #r.cmd("s 0x00400400")
    print(r.cmd("pd"))
    #  initialize stack machine for emulation
    r.cmd("aeim")
    #print("stack machine created")
    #  working commands: 'ar,' - table view; 'ar' - register and value
    print(r.cmd("ar"))
    print(r.cmd("ad@r:SP"))
    #print(r.cmd("ad@r:SP"))
   # print("aeim")
    #registers = r.cmd("aer")
    #print(registers)
    aesu = 'aesu 0x' + hex(func.offset + func.length-1)[2:].zfill(8)
    #print(aesu)
    #  emulate from the start of the func until specified address
    print(r.cmd(aesu))
    #print("HI")
    #print(r.cmd())
    print(r.cmd("ar"))
    #print("Expelliarmus")
    print(r.cmd("ad@r:SP"))
    #print("Lumos")
    print(r.cmd("ad@r:SP"))
    #print("Bye")


def emulate_function_with_params(func, binary):
    r = r2pipe.open(binary)
    addr = "0x"+hex(func.offset)[2:].zfill(8)
    s = 's '+addr
    r.cmd(s)
    print(r.cmd("pd"))
    #  initialize stack machine for emulation
    r.cmd("aeim")
    for reg in func.params:
        r.cmd(f'aer {reg} = {func.params[reg]}')
    #  working commands: 'ar,' - table view; 'ar' - register and value
    print(r.cmd("ar"))
    print(r.cmd("ad@r:SP"))
    aesu = 'aesu 0x' + hex(func.offset + func.length-1)[2:].zfill(8)
    #  emulate from the start of the func until specified address
    print(r.cmd(aesu))
    print(r.cmd("ar"))
    print(r.cmd("ad@r:SP"))
    print(r.cmd("ad@r:SP"))
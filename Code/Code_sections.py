import r2pipe
import Code.FunctionClass

def get_functions_data(binary):
    r = r2pipe.open(binary)
    r.cmd('aa')
    afl = r.cmd("afl")
    pdf = r.cmd("pdf")
    #print(pdf)
    lines = pdf.split("\n")
    functions = []
    counter = 1
    for func in lines:
        if len(func) > 0:
            data = func.split(" ")
            shortened_list = [x for x in data if x != '']
            # print(shortened_list[3])
            f = Code.FunctionClass.Function(shortened_list[3], int(shortened_list[0], 16), int(shortened_list[2]), {})
            # print(f.name)
            #if len(functions) > 1:
            functions.append(f)
            # print(r.cmd("afa"))
  #  for func in functions:
   #     r.cmd(f's {hex(func.offset)}')
    #    #  initialize stack machine for emulation
     #   r.cmd("aeim")
      #  registers = r.cmdj("aer")
       # print(f"*********************************\n{registers}\n*********************")
    r.quit()
    return functions


def disassembler(binary, func_dict, func_id):
        r = r2pipe.open(binary)
        jinstr = r.cmdj("pdj")
        jinstr = r.cmdj("pdj")
        assembly_string = ""
        func = func_dict[func_id]
        func_end = func.offset+func.length
        #print(f'{func.offset} {func_end}')
        for line in jinstr:
            if ('offset' in line and 'bytes' in line and 'opcode' in line) and (func.offset <= line["offset"]) and (line["offset"]<func_end):
                #print("Alohomora")
                assembly_string += f"0x{line['offset']:x}  {line['bytes']}  {line['opcode']}\r\n"
        r.quit()
        return assembly_string


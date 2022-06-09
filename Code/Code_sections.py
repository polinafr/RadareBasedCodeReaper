import r2pipe
import Code.FunctionClass

def get_functions_data(binary):
    r = r2pipe.open(binary)
    r.cmd('aa')
    afl = r.cmd("afl")
    pdf = r.cmd("pdf")
    print(pdf)
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
    return functions

#f = get_functions_data("Examples/ConsoleApplication1.exe")
#for i_ in f:
   # print(f'{i_.offset}  {i_.length}  {i_.name}')
    #print(i_.to_string())


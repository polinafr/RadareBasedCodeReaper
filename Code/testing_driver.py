from Code import FunctionClass, Code_sections, Emulations

funcs = Code_sections.get_functions_data('../Examples/sample_exe64.elf')
# #print(len(funcs))
# funcs[-1].add_arg('rcx', 10)
# funcs[-1].add_arg('rax', 12)
# Emulations.emulate_function_with_params(funcs[-1], '../Examples/sample_exe64.elf')
var = Code_sections.disassembler('../Examples/sample_exe64.elf', funcs, 0)
print(var)
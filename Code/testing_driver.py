from Code import FunctionClass, Code_sections, Emulations

funcs = Code_sections.get_functions_data('../Examples/sample_exe64.elf')
#print(len(funcs))
Emulations.emulate_function(funcs[-2], '../Examples/sample_exe64.elf')
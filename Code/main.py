import sys
import Code.FunctionClass
import Code.Code_sections
import Disassemblers.ELFDisassembler
import pe_disassembler
import pathlib

def emulate_function(function_dictionary, executable):
    pass

def show_assembly(function_dictionary, binary):
    extension = pathlib.Path(binary).suffix
    #func = None
    func_index = get_desired_function(function_dictionary)
    func = function_dictionary[func_index]
    if extension == '.exe':
        pass
    elif extension == '.elf':
        disasm = Disassemblers.ELFDisassembler.ELFDisassembler(binary)
        print(disasm.get_function_by_address_and_size(func.offset, func.length))
    print("To update the arguments list for the function, enter a\nTo emulate this function, enter e\n"
          "To change the function's name, enter n\nTo disassemble another function, enter d\n"
          "To return to the main menu enter m")
    current_choice = input()
    if current_choice == 'a':
        update_arguments(function_dictionary, func_index)
    elif current_choice == 'e':
        emulate_function(function_dictionary, binary, func_index)
    elif current_choice == 'n':
        print("Enter the new function's name")
        function_dictionary[func_index].rename(input())
       # get_main_choice(function_dictionary, binary)
    elif current_choice == 'd':
        show_assembly(function_dictionary, binary)
    elif current_choice == 'm':
        get_main_choice(function_dictionary, binary)


def update_arguments(function_dictionary, func_index):
    while True:
        print("Please enter the register name and the argument, separated by blankspace;\n"
              "If the argument is passed on stack please enter them in upside-down manner, named stack1, stack2 etc")
        param = input().split(' ')
        function_dictionary[func_index].add_arg(param[0], param[1])
        print("Arguement sucessfully added. Do yo want to enter another one? (y/n)")
        if input() == 'n':
            break


def get_desired_function(function_dictionary):
    while True:
        print("Please enter the number of function to show its instruction")
        func_id = int(input())
        if func_id not in function_dictionary:
            print("The number doesn't belong to any function")
        else:
            return func_id
            break


def get_main_choice(function_dictionary, executable):
    while True:
        print('The functions found are: ')
        print(f"{'number'}  {'offset'}  {'length'}  {'name'}  {'parameters known to program'}")
        for i in range(1, len(functions)+1):
            print(f'{str(i)} {function_dictionary[i].to_string()}')
        print("To see the function's instructions, enter 1\nTo emulate the function, enter 2\nTo exit, enter X")
        choice = input()
        if choice == '1':
            show_assembly(function_dictionary, executable)

        elif choice == '2':
            emulate_function(function_dictionary, executable)
        elif choice == 'X':
            break
        else:
            print("The entered code is wrong")


if __name__ == "__main__":
    num_of_arguments = len(sys.argv)
    if num_of_arguments == 2:
        executable = sys.argv[1]
        functions = Code.Code_sections.get_functions_data(executable)
        function_dictionary = {i: functions[i-1] for i in range(1, len(functions)+1)}
        get_main_choice(function_dictionary, executable)




    else:
        print("You should enter the file's path")
    #for i, arg in enumerate(sys.argv):
     #   print(f"Argument {i:>6}: {arg}")
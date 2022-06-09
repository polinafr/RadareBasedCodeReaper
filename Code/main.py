import sys
import Code.FunctionClass
import Code.Code_sections
import Code.Emulations

try:
    import r2pipe
except ImportError:
    print("Error with the import r2pipe")
    exit(-123)


def emulate_function(function_dictionary, executable, func_index=None):
    try:
        if not func_index:
            func_index = get_desired_function(function_dictionary)
        if len(function_dictionary[func_index].params) == 0:
            Code.Emulations.emulate_function(function_dictionary[func_index], executable)
        else:
            Code.Emulations.emulate_function_with_params(function_dictionary[func_index], executable)
        return
    except:
        print("Error with the emulation")


def show_assembly(function_dictionary, binary):
    func_index = get_desired_function(function_dictionary)
    result_disassembler = Code.Code_sections.disassembler(binary, function_dictionary, func_index)
    if result_disassembler != "":
        print(result_disassembler)  # func 3 work for example
    else:
        print("This function can't be disassembled")

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
        print("Please enter the register name and the argument, separated by blankspace;\n")
        param = input().split(' ')
        if len(param) == 2:
            function_dictionary[func_index].add_arg(param[0], param[1])
            print("Argument successfully added. Do yo want to enter another one? (y/n)")
            if input() == 'n':
                break
        else:
            print("You have to enter two arguments!")



def get_desired_function(function_dictionary):
    while True:
        print("Please enter the number of function to show its instruction")
        func_id = int(input())
        if func_id not in function_dictionary:
            print("The number doesn't belong to any function")
        else:
            return func_id


def get_main_choice(function_dictionary, executable):
    while True:
        # print(len(functions))
        # print(f"{'number'}  {'offset'}  {'length'}  {'name'}  {'parameters known to program'}")
        print("Welcome")
        if (len(functions) > 0):
            print('The functions found in the program are: ')
            for i in range(1, len(functions) + 1):
                print("Function " + str(i))
                print({function_dictionary[i].to_string()})
                # print(f'{str(i)} {function_dictionary[i].to_string()}')
        else:
            print("No function in the program")
            break

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
        function_dictionary = {i: functions[i - 1] for i in range(1, len(functions) + 1)}
        get_main_choice(function_dictionary, executable)




    else:
        print("You should enter the file's path")
    # for i, arg in enumerate(sys.argv):
    #   print(f"Argument {i:>6}: {arg}")

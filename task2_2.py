"""task2 """
import json
def read_file(file):
    """
    Reads the file and parses the dictionary or list with info.
    """
    with open(file, "r") as file:
        line = json.load(file)
    return line

def organise_data(line):
    """
    Reads the line and navigates through it's information.
    """
    if isinstance(line, list):
        print("""This is a list. Show all list or one element?
        s - show all
        <number> - type index of element""")
        def repeat_list(line):
            print("please, enter the right value")
            answer1 = input(">>> ")
            if isinstance(answer1, int):
                print(line[answer1])
                organise_data(line[answer1])
            elif answer1 == "s":
                print(line)
                organise_data(line)
            else:
                repeat_list(line)
        repeat_list(line)
    elif isinstance(line, dict):
        print("""This is a dict. Show all keys and values or one value?
        s - show all keys
        "<key>" - type key of specific value in brackets """)
        def repeat_dict(line):
            print("please, enter the right value")
            answer2 = input(">>> ")
            if answer2 in line.keys():
                print(line[answer2])
                organise_data(line[answer2])
            elif answer2 == "s":
                print(line.keys())
                organise_data(line)
            else:
                print("No key in dict")
                repeat_dict(line)
        repeat_dict(line)

if __name__ == "__main__":
    print("Enter path to your file")
    try:
        file = input(">>> ")
        read_file(file)
        organise_data(read_file(file))
    except FileNotFoundError and FileExistsError:
        print('Oops, no file')
        quit()
    except Exception:
        print("Something else went wrong, now think about your behavior")
        quit()
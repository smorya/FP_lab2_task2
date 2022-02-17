import json

def read_file(file):
    with open(file, "r") as file:
        line = json.load(file)
    return line

def organise_data(line):
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
                print(line[answer2].keys())
                organise_data(line)
            elif answer2 == "s":
                print(line.keys())
                organise_data(line)
            else:
                print("No key in dict")
                repeat_dict(line)
        repeat_dict(line)

if __name__ == "__main__":
    file = '/Users/mskoropad/OPlabs/OPlabs2/lab2task3/task3_twitter_api/twitter_json/frienfs_list_Obama.json'
    read_file(file)
    organise_data(read_file(file))
from os.path import dirname, realpath
import shutil


def replace_file_content(path: str, day_number: str):
    with open(path, "r") as file :
        filedata = file.read()
    filedata = filedata.replace("{day_number}", day_number)
    with open(path, "w") as file:
        file.write(filedata)


current_path = dirname(realpath(__file__))
tests_path = f"{current_path}/tests/"
src_path = f"{current_path}/src/"
input_path = f"{current_path}/input/"
day_number = input("Day #: ")

test_file_path = f"{tests_path}/test_day_{day_number}.py"
shutil.copy(f"{current_path}/test_day.template", test_file_path)
replace_file_content(test_file_path, day_number)

file_path = f"{src_path}/day_{day_number}.py"
shutil.copy(f"{current_path}/day.template", file_path)
replace_file_content(file_path, day_number)

test_input_file_path = f"{input_path}/day-{day_number}-test"
open(test_input_file_path, "a").close()

input_file_path = f"{input_path}/day-{day_number}"
open(input_file_path, "a").close()

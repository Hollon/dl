# This is a sample Python script.
# -*- coding: utf-8
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import torch

def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    print(torch.cuda.is_available())
    print(torch.cuda.get_device_name(0))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

"""
File: Milestone1.py
-----------------------
This file is to test the code for 
babyname.py milestone 1

"""
import sys


def add_data_for_name(name_data, year, rank, name):
    """
    :param name_data:
    :param year:
    :param rank:
    :param name:
    :return: None
    """
    print('rank'+rank)
    print('==============================================================')
    if name in name_data:
        if year in name_data[name]:
            if rank < name_data[name][year]:
                name_data[name][year] = rank
        else:
            name_data[name][year] = rank
    else:
        name_data[name] = {year, rank}


# ------------- DO NOT EDIT THE CODE BELOW THIS LINE ---------------- #

def test1():
    name_data = {'Kylie':{'2010':'57'}, 'Nick':{'2010':'37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    print('--------------------test1----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test2():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test2----------------------')
    print(str(name_data))
    print('-----------------------------------------------')



def test3():
    name_data = {'Kylie': {'2010': '57'},'Sammy': {'1980':'451','1990': '200'}}
    add_data_for_name(name_data, '1990', '100', 'Sammy')
    print('-------------------test3-----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test4():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    print('pass 1')
    add_data_for_name(name_data, '1990', '100', 'Sammy')
    print('pass 2')
    add_data_for_name(name_data, '1990', '200', 'Sammy')
    print('pass 3')
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('pass 4')
    print('--------------------test4----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def main():
    args = sys.argv[1:]
    if len(args) == 1 and args[0] == 'test1':
        test1()
    elif len(args) == 1 and args[0] == 'test2':
        test2()
    elif len(args) == 1 and args[0] == 'test3':
        test3()
    elif len(args) == 1 and args[0] == 'test4':
        test4()


if __name__ == "__main__":
    main()
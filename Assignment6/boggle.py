"""
File: boggle.py
Name: Sarah Lin
----------------------------------------
this program find out the boggle answer
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'  # the dic name

# Global variable
Count = 0  # the num of len(ans)


def main():
	"""
	this play boggle
	"""
	dic = read_dictionary([])
	row_lst = input_word()
	ans = []
	for row in range(4):
		for col in range(4):
			play(row, col, '', dic, row_lst, ans, [])
	print('There are ' + str(Count) + ' words in total.')


def play(current_row, current_col,  visit, dic, row_lst, ans, v_lst):
	"""
	this function find the correct word inside the row_lst
	:param current_row: (int) the current_word row
	:param current_col: (int) the current_word col
	:param visit: (str) the visited string
	:param dic: (dictionary) the correct word
	:param row_lst: (list) the user's input
	:param ans: (list) the total answer
	:param v_lst: (list) have visited row and col
	:return: None
	"""
	global Count
	if -1 < current_col < 4 and -1 < current_row < 4 and [current_row, current_col] not in v_lst:  # if not out of range
		visit += row_lst[current_row][current_col]  # add
		if not has_prefix(visit, dic):  # if visit in dic
			return
		else:
			for row in range(-1, 2):  # runs -1, 0, 1
				for col in range(-1, 2):  # runs -1, 0, 1
					if row == 0 and col == 0:  # if not itself
						pass
					else:
						v_lst.append([current_row, current_col])
						play(current_row + row, current_col + col, visit, dic,
						row_lst, ans, v_lst)
						v_lst.pop()
						if len(visit) >= 4:
							if visit not in ans:
								if visit in dic:
									ans.append(visit)
									Count += 1
									print('Found "' + str(visit) + '"')


def input_word():
	"""
	:return row_list: (list) the list of the user enter
	"""
	row_list = []
	for i in range(4):
		row = input(str(i+1) + ' row of letters: ')  # input word
		lst = row.split(' ')  # split the row
		if not len(lst) == 4 or not len(row) == 7:  # if format
			while not len(lst) == 4 or not len(row) == 7:  # enter until correct
				print('Illegal input')
				row = input(str(i + 1) + ' row of letters: ')
				lst = row.split(' ')
		row.lower()
		row_list.append(row.split(' '))
	return row_list


def read_dictionary(dic):
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	:param dic: (dictionary) a blank dic to contain the words in dictionary.txt
	"""
	with open(FILE, 'r') as f:
		for line in f:
			if not line == '':
				dic.append(line.strip())
	return dic


def has_prefix(sub_s, dic):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	if sub_s == None:
		return True
	for word in dic:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()

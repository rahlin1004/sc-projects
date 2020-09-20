"""
File: largest_digit.py
Name: Sarah Lin
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	"""
	this program help you find the biggest num
	"""
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, the num to use
	:return: the biggest num in n
	"""
	if n < 0:  # if n have " - "
		n = -n
	return helper(n)


def helper(n):
	"""
	this is the helper of find_largest_digit
	:param n: int, the num to use
	:return: the biggest num in n
	"""
	if n < 10:
		return n
	else:
		if n % 10 < (n % 100 - n % 10) // 10:  # if the last #1 num smaller than the last #2 num
			return find_largest_digit(n // 10)  # pop the last #1 num
		else:  # if the last #1 num bigger than the last #2 num
			return find_largest_digit(n // 100 * 10 + n % 10)  # pop the last #2 num


if __name__ == '__main__':
	main()

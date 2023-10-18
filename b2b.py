# Python file to change numbers base
# Writed in a bus
import sys

"""The conversions work with 2 methods:
 The subtraction method to convert a base 10 number to a base X number.
 The Decimal Representation to convert a base X number to a base 10 number.

 For convert from bases besides 10, like from base 8 to base 2:
 it will first converts to base 10 and than go to the wanted base.
 Ex: if you wanna convert 11001 from Base 2 to Base 8, the program will do:
 	1: 11001 from Base 2 to Base 10, resulting in 25.
 	2º: 25 from Base 10 to base 8, resulting in 31.

 					in resume:
 	     	b2 11001 -> b10 25 -> b8 31
 """
def change(num, fromB, to):

	# ------------------------------------------------------------
    # 1 - input analysis and error raising if necessary:

	# 1.1 - Checking if the input number is valid to the base argument.
	dgtsFrom = list(range(fromB))
	for i in num:
			if i not in str(dgtsFrom):
				if i not in 'ABCDEF':
					return 2
			if i in 'ABCDEF' and fromB <= 10:
					return 2

	# 1.2 - The algorithm just accept bases between 2 and 16 | {x : 2 <= x <= 16}
	if (fromB > 16 or to > 16) or (fromB < 2 or to < 2):
		return 1

	# --------------------------------------------------
	# 2 - Formating the input for use
	# The number input comes as string, if none hexadecimal characters are in the input, we can use it as INT instead
	try:
		num = int(num)
	except:
		pass


	# --------------------------------------------------
	# 3 - Converting the number
	print(f'\nConverting number {num} from Base {fromB} to Base {to}.')

	# 3.1 - Using the subtraction method to convert from a base 10 number
	dgts = list(reversed(range(to)))
	def from10(num, to):

		convNum = ''
		n = 0
		index = 0
		# 3.1.1 - In this method, we first must discover the number of digits of the number in the new base, for it: BaseTo ** Position >= BaseToNumber. Ex: 2**4 >= 10, Base2 10 has 4 digits.
		while True:
			if to**index == num:
				n = index
				break
			elif to**index > num:
				n = index - 1
				break
			index += 1

		nHold = n #Just to show the length after.

		# 3.1.2 - Doing the formula for each number in the new base charset until we have the full number in the new base and num == 0.
		while num > 0:
			for i in dgts:
				if i*(to**n) <= num:
					num -= i*(to**n)
					n -= 1
					#Hexadecimal digits change
					if i >= 10:
						convNum += str(i).replace('10', 'A').replace('11', 'B').replace('12', 'C').replace('13','D').replace('14','E').replace('15','F')
						break
					convNum += str(i)
					break

		while n != -1:
			convNum += '0'
			n -= 1

		return (convNum, nHold + 1)


	# 3.2 - Getting thebnumber in base 10 by decimal representation.
	def to10(num, fromB):

		#Start from the less significant digit
		num = list(reversed([i for i in list(str(num))]))
		convNum = 0

		for index, n in enumerate(num):
			#Hexadecimal digits change
			if str(n) in 'ABCDEF':
				n = n.replace('A', '10').replace('B', '11').replace('C', '12').replace('D','13').replace('E','14').replace('F','15')
			convNum += int(n)*(fromB**index)

		return (convNum, len(str(convNum)))

	# --------------------------------------------------
	# 4 - Showing the results
	def showResults(results):
		print('_____________________________________________')
		print(f'Resulted number:', results[0])
		print('Number of digits:', results[1], '\n')
		return 0

	if fromB == 10:
		results = from10(num, to)
		showResults(results)

	elif to == 10:
		results = to10(num, fromB)
		showResults(results)

	elif to != 10 and fromB != 10:
		resultA = to10(num, fromB)
		resultB = from10(resultA[0], to)
		showResults(resultB)


if  __name__ == "__main__":
	# Recive a string number (because of Hexadecimal Chars) /
	# And 2 Ints, FromB, which is the number base and /
	# To, the base you wanna to convert to.
	# in the script, the Number will be converted to int for the operations in the methods.
	# The return will be a int representing a execution code.
	response = change(str(sys.argv[1]).upper(), int(sys.argv[2]), int(sys.argv[3]))
	if response == 1:
		print('Only accept bases between 16 and 2')
	elif response == 2:
		print('Invalid Input Number')
	elif response == 0:
		pass

	# 2 - Input error
	# 1 - Invalid base (don't handled)
	# 0 - Successful execution

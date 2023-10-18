# Python file to change numbers base
# Writed in a bus
import sys

def change(num, fromB, to, type = "n"):
	print('')
	'''Cheking if the input is valid'''
	dgtsFrom = list(range(fromB))
	for i in str(num):
			if int(i) not in dgtsFrom:
				exit()

	'''Get the base digit set'''
	dgts = list(reversed(range(to)))


	print(f'Converting number {num} from Base {fromB} to Base {to}.')

	'''using decimal arithmetics to change the base if the origen base is 10'''
	def from10(num, to):
		'''Get the number of digits in the new base'''


		convNum = ''
		n = 0
		index = 0
		while True:
			if to**index == num:
				n = index
				break
			elif to**index > num:
				n = index - 1
				break
			index += 1

		nHold = n

		'''using subtraction method'''
		while num > 0:
			for i in dgts:
				if i*(to**n) <= num:
					num -= i*(to**n)
					n -= 1
					convNum += str(i)
					# print(f'num: {num}, n: {n}, conv: {convNum}')
					break

		while n != -1:
			convNum += '0'
			n -= 1

		return (convNum, nHold + 1)


	def to10(num, fromB):

		num = reversed([int(i) for i in list(str(num))])
		convNum = 0

		for index, n in enumerate(num):
			convNum += n*(fromB**index)

		return (convNum, len(str(convNum)))


	def showResults(results):
		print('---------------------')
		print(f'Resulted number:', results[0])
		print('Number of digits:', results[1])


	if fromB == 10:
		results = from10(num, to)
		showResults(results)

	elif to == 10:
		results = to10(num, fromB)
		showResults(results)

	elif to != 10 and fromB != 10:
		# exemple: 10 from base 2 to base 8
		resultA = to10(num, fromB)
		resultB = from10(resultA[0], to)
		showResults(resultB)


if  __name__ == "__main__":

	try:
		change(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
	except:
		print('Invalid Input Number')


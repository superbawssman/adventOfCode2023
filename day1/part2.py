def filter_for_digits(character):
	numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	if character in numbers:
		return True
	else:
		return False


input = open("input_file.txt", 'r')
#input = "1abc2\n2abc1"
counter = 0
for line in input:
	line_forward = list(line)
	line_backward = list(line)
	line_backward.reverse()
	print(line_forward)
	print(line_backward)
	forward_filtered = list(filter(filter_for_digits, line_forward))
	#print(forward_filtered)
	backward_filtered = list(filter(filter_for_digits, line_backward))
	#print(backward_filtered)
	first_digit = forward_filtered[0]
	last_digit = backward_filtered[0]
	print(first_digit)
	print(last_digit)
	number_string = first_digit + last_digit
	number_int = int(number_string)
	counter = counter + number_int
print("final result is: " + str(counter))


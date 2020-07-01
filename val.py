def input_validation(prompt):
	score1 = input_validation('Enter the score for the first test: ')
	score2 = input_validation('Enter the score for the second test: ')
	while True:
		answer = input(prompt)
		try:
			score = float(answer)
		  if 0 <= score <= 100:
				return score
		  else:
		    print('Score cannot be less than 0 or greater than 100!')
		except ValueError:
			print ('That is not a test score.')

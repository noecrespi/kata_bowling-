from main import calculaPuntosTotales


if __name__ == '__main__' :
    
	# simple test
	assert calculaPuntosTotales('12345123451234512345')== 60
	# test symbol -, no pins knocked
	assert calculaPuntosTotales('9-9-9-9-9-9-9-9-9-9-')== 90
	assert calculaPuntosTotales('9-3561368153258-7181')== 82

	'''
	If in two tries he knocks them all down, this is called a “spare” and his score for the frame is ten plus the number of pins knocked down on his next throw (in his next turn).

	If he gets a spare or strike in the last (tenth) frame, the bowler gets to throw one or two more bonus balls, respectively. - These bonus throws are taken as part of the same turn. If the bonus throws knock down all the pins, the process does not repeat: the bonus throws are only used to calculate the score of the final frame.
	'''
	assert calculaPuntosTotales('5/5/5/5/5/5/5/5/5/5/5')== 150
	assert calculaPuntosTotales('9-3/613/815/-/8-7/8/8')== 131

	'''
	If on his first try in the frame he knocks down all the pins, this is called a “strike”. His turn is over, and his score for the frame is ten plus the simple total of the pins knocked down in his next two rolls.

	If he gets a spare or strike in the last (tenth) frame, the bowler gets to throw one or two more bonus balls, respectively. - These bonus throws are taken as part of the same turn. If the bonus throws knock down all the
	pins, the process does not repeat: the bonus throws are only used to calculate the score of the final frame.
	'''
	assert calculaPuntosTotales('X9-9-9-9-9-9-9-9-9-')== 100
	# two extra final rolls
	assert calculaPuntosTotales('9-9-9-9-9-9-9-9-9-X9-')== 100
	assert calculaPuntosTotales('X9-X9-9-9-9-9-9-9-')== 110
	assert calculaPuntosTotales('XX9-9-9-9-9-9-9-9-')== 120
	# three strikes in a row is a triple
	assert calculaPuntosTotales('XXX9-9-9-9-9-9-9-')== 141
	# two strikes in extra rolls
	assert calculaPuntosTotales('9-9-9-9-9-9-9-9-9-XXX')== 111
	# 12 strikes is a “Thanksgiving Turkey”
	assert calculaPuntosTotales('XXXXXXXXXXXX')== 300
	# spare in extra roll
	assert calculaPuntosTotales('8/549-XX5/53639/9/X')== 149
	# spare in extra roll
	assert calculaPuntosTotales('X5/X5/XX5/--5/X5/')== 175

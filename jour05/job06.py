def math(note):
	if note < 40:
		print(note," négatif")
	elif note >= 40:
		if note % 5 >= 3 or note % 5 == 0:
			new_grade = note
			while new_grade % 5 != 0:
				new_grade+=1
			print(new_grade,"positif")
		else:
			new_grade = note
			print(new_grade,"c'est bien continue")

math(5)
math(5)
math(82)
math(83)
math(100)
math(99)
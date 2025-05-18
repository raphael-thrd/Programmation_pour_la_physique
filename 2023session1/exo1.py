for x in range(2,100):
	for y in range(2,100):
		for a in range(2,10):
			for b in range(2,10):
				equ=x**a-y**b
				if equ==-1:
					print(f"solution: x={x}, b={b}, y={y}, a={a}")

from tabulate import tabulate

COLORS = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'grey', 'white', 'gold', 'silver']
TOLL = {
	'gold': 5.0,
	'silver': 10.0,
	'brown': 1.0,
	'red': 2.0,
	'orange': 3.0,
	'green': 0.5,
	'blue': 0.25,
	'purple': 0.1,
	'grey': 0.05,
}
HEADER = ['Colors', 'Result', 'Tolleranza', 'Tot OHM', 'Min OHM', 'Max OHM']

def calculate(colorList):
	result = ''
	colorList.reverse()
	tolleranza = TOLL[colorList[0]]
	moltiplic = colorList[1]
	colorList.reverse()
	moltiplic = COLORS.index(moltiplic)
	colorList.pop()
	colorList.pop()

	for color in colorList:
		result += str(COLORS.index(color))
	result = int(result)
	value = result * (10 ** moltiplic)
	totOhm = (value / 100) * tolleranza
	table = [[', '.join(colorList), value, str(tolleranza) + '%', totOhm, value - totOhm, value + totOhm]]
	print(tabulate(table, HEADER, tablefmt="pretty"))



if __name__ == "__main__":
	res = input('Write the colors in order separated by a space: ')
	resColors = res.split(' ')
	if not all(elem.lower() in COLORS  for elem in resColors):
		print('A color is not allowed')
		exit(1)
	if not len(resColors) >= 3:
		print('Not enough colors')
		exit(1)
	calculate(resColors)

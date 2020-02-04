xvals = [float(n) for n in input("Write all X values: ").split(' ')]
yvals = [float(n) for n in input("Write all Y values: ").split(' ')]
xlenght = float(input("X lenght: "))
ylenght = float(input("Y lenght: "))
xscale , yscale = max(xvals) / xlenght , max(yvals) / ylenght
print(f"\nX Scale: {xscale}  Y Scale: {yscale}")
i = 1
for x,y in zip(xvals,yvals):
  print(f"{i})   X: {x / xscale} Y: {y / yscale}")
  i = i + 1

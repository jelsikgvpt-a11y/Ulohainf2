start = int(input("Odkiaľ: "))
end = int(input("Pokiaľ: "))
if start > end:
	start, end = end, start

import math
for i in range(start, end+1):
	print(i, round(math.sqrt(i), 2))


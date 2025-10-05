start = int(input("Odkiaľ: "))
end = int(input("Pokiaľ: "))
if start > end:
    start, end = end, start
count = sum(1 for i in range(start, end+1) if i % 8 == 0)
print(count)

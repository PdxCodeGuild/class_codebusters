
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

c = max(data)
row = []
while c > 0:
    for i in range(len(data)):
        x = data[i]  # for troubleshooting
        if data[i] >= c:
            row.append(' X')
        else:
            row.append(' ')
            row.append('')
    peak = ' '.join(row)
    print(peak)
    c -= 1
    row = []
print(data)

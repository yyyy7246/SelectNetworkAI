with open('D:\desultnew.txt', 'r') as f:
    lines2 = f.readlines()
for i in range(0, len(lines2)):
    lines2[i] = lines2[i].rstrip('\n')
    lines2[i] = lines2[i].strip('[]')
    lines2[i] = lines2[i].split(',')
for i in range(0, len(lines2)):
    for j in range(0,3):
        if 'e' in lines2[i][j]:
            lines2[i][j] = 0
        elif float(lines2[i][j][0:5]) < 0.5 :
            lines2[i][j] = 0
        elif float(lines2[i][j][0:5]) > 0.5 :
            lines2[i][j] = 1
for i in range(0,len(lines2)):
    print(lines2[i])

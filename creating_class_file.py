line_format = '{:20} {}'
sum_of_score = 0
y = []

with open('src.txt', 'r', encoding='utf-8') as src:
    with open('dst.txt', 'w', encoding='utf-8') as dst:
        if not src.closed:
            print('file open')
        for line in src:
            line = line.split()
            surname_n = line[1] + ' ' + line[0][0] + '.'
            scores = line[2:]
            y.append(scores)
            sum_of_score += sum([int(score) for score in scores])
            average_score = round(sum([int(score) for score in scores]) / len(scores), 2)
            if average_score < 5:
                print(line_format.format(surname_n, average_score))
            dst.write(line_format.format(surname_n, average_score))
            dst.write('\n')

print("Средний бал класса: ", round(sum_of_score / len(sum(y, [])), 2))
# print(surname_n)
# print(scores)
# print(average_score)
# print(sum_of_score)
# print(y)
# print(len(sum(y, [])))

if src.closed:
    print('file closed')

scores = [55,43,78,38,96, 51]

for score in scores:
    if score >= 80:
        print(str(score) + '点:' + '合格')
    else:
        print(str(score) + '点:' + '不合格')
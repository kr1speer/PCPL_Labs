def field(lst, *args):
    if len(args) == 1:
        key = args[0]
        for item in lst:
            if key in item and item[key] is not None:
                yield item[key]
    else:
        for item in lst:
            result = {}
            for key in args:
                if key in item and item[key] is not None:
                    result[key] = item[key]
            if result:
                yield result

def test():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    print("Один аргумент:")
    for value in field(goods, 'title'):
                print(value)

    print("\nНесколько аргументов:")
    for value in field(goods, 'title', 'price'):
                print(value)

def parse(filename):
    def group(seq, sep):
        g = []
        for el in seq:
            if el[0] == sep:
                yield g
                g = []
            g.append(el)
        yield g

    links = {}
    with open(filename) as f:
        lines = f.readlines()

        groups = list(group(lines, "#"))
        del groups[0]

        for group in groups:
            cat = group[0][2:].rstrip()
            del group[0]
            links[cat] = []
            for item in group:
                i = item.split(' ')
                url = i[0]
                name = i[1].rstrip()
                ltype = i[2].rstrip()
                if ltype == '2':
                    color = '#98C5CD'
                    size = '1.8'
                elif ltype == '3':
                    color = '#72B691'
                    size = '2.4'
                else:
                    print("Syntax error.")

                links[cat].append({'url': url, 'name': name, 'size': size, 'color': color})
    return links

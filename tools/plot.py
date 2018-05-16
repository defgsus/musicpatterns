

def dump_values(values):
    mi, ma = int(min(values)), int(max(values))

    height = ma-mi+1
    x_offset = max(len(str(ma)), len(str(mi))) + 3

    plot = dict()

    for i in range(0, ma+1-mi):
        plot[(0, height-1-i)] = "%s" % (i+mi)
        plot[(x_offset-2, height-1-i)] = "-+"

    for i, v in enumerate(values):
        plot[(x_offset+i, height-1-(v-mi))] = "*"

    for i in range(0, len(values), 8):
        plot[(x_offset+i-1, height)] = "|%s" % i

    width = max(t[0]+len(plot[t]) for t in plot)
    height = max(t[1] for t in plot)

    lines = [[" " for x in range(width+1)] for y in range(height+1)]
    for t in plot:
        val = plot[t]
        for i, v in enumerate(val):
            lines[t[1]][t[0] + i] = v

    print("\n".join("".join(line) for line in lines))
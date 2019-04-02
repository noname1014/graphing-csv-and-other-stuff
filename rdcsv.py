def read_csv(filename):
    file_in = open(str(filename), "r")
    data = []
    attrs = file_in.readline()
    attrs = attrs.split(",")
    del attrs[0]
    attrs.insert(0, "index")
    for i in range(1, len(attrs), 1):
        attrs[i] = str(attrs[i].lower()).rstrip()
    line_num = 0
    for line in file_in:
        if line_num != 0:
            datapoint = {}
            i = 0
            line = line.split(",")
            datapoint["line"] = line_num
            for key in attrs:
                datapoint[attrs[i]] = line[i].rstrip()
                i += 1
            data.append(datapoint)
        line_num += 1
    return data

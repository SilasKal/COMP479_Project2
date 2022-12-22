def output(input_list, filepath):
    """
    writes items of in a list of tuples into a file
    :param input_list: list of tuples
    :param filepath: filename of output
    """
    with open(filepath, 'w') as f:
        for item in input_list:
            f.write(item[0] + ' ' + str(item[1]))
            f.write('\n')
    f.close()


def diff_percent(value1, value2):
    """
    returns difference between value1 and value2 in percent
    :param value1: first value
    :param value2: second value
    :return: difference between the two values in percent rounded to two decimal places
    """
    try:
        return round((value1 - value2) / value1 * 100, 2)
    except ZeroDivisionError:
        return 0


def output_dic(input_dic, filepath):
    """
    writes items from a dictionary into a file
    :param input_dic: dictionary with key that are string and values that are lists of strings
    :param filepath: filename of output
    :return:
    """
    with open(filepath, 'w') as f:
        for key, value in input_dic.items():
            f.write(key + ' ')
            for item in value:
                f.write(item + ' ')
            f.write('\n')
    f.close()


def print_table(title_columns, rows):
    """
    prints table with given colum titles and rows to the console
    :param title_columns: titles of the columns as a List
    :param rows: values of the rows in a List of Lists
    """
    table = [title_columns]
    table.extend(rows)
    for row in table:
        print("{:<13} {:<16} {:<22} {:<6} {:<20} {:<22} {:<6}".format(*row))


def read_index(filepath):
    """
    extracts index as a dictionary from a txt file
    :param filepath: filepath of index
    """
    index = {}
    try:
        with open(filepath) as file:
            line = file.readline()
            split_line = line.split(sep=' ')
            if split_line:
                index[split_line[0]] = split_line[1:-1]
            while line:
                line = file.readline()
                split_line = line.split(sep=' ')
                if split_line:
                    index[split_line[0]] = split_line[1:-1]
        file.close()
        return index
    except FileNotFoundError:
        print('No index found at given filepath.')
        return {}

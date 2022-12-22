
import nltk
from module1 import read_extract
from helper_functions import output, output_dic


def naive_indexer(input_files=[], output_file='sorted_filtered_F.txt'):
    """
    processes given input files and returns a filtered list of term-document pairs
    :param input_files: list of filepath of input files
    :param output_file: filename output file
    :return: filtered list of term-document pairs
    """
    F = []
    if not input_files:
        for i in range(22):
            if i < 10:
                dict_000 = read_extract('reuters21578/reut2-00' + str(i) + '.sgm')
            else:
                dict_000 = read_extract('reuters21578/reut2-0' + str(i) + '.sgm')
            print('document ' + str(i))
            for article in dict_000.keys():
                tokens = nltk.word_tokenize(dict_000[article])
                tokens = [token for token in tokens if any(charac.isalnum() for charac in token) and token != '']
                F.extend(parser(tokens, article))
        F_filtered = sorted(list(set(F)), key=lambda x: (x[0], int(x[1])))  # sort and remove duplicates
        output(F_filtered, output_file)
        return F_filtered
    else:
        for file in input_files:
            dict_000 = read_extract(file)
            for article in dict_000.keys():
                tokens = nltk.word_tokenize(dict_000[article])
                tokens = [token for token in tokens if any(charac.isalnum() for charac in token) and token != '']
                F.extend(parser(tokens, article))
        F_filtered = sorted(list(set(F)), key=lambda x: (x[0], int(x[1])))  # sort and remove duplicates
        print('finished sorting, removing duplicates')
        output(F_filtered, 'F_filtered_sorted.txt')
        return F_filtered


def parser(tokens, documentID):
    """
    accepts a list of tokens and a documentID and returns a List of term-documentID pairs
    :param tokens: list of tokens to be processed
    :param documentID: NEWID of the article from which the tokens where extracted
    :return: list F consisting of term-documentID pairs without duplicates and sorted
    """
    F = []
    for token in tokens:
        F.append((token, documentID))
    return F


def create_index(F, output_file='index_uncompressed.txt'):
    """
    crates index from file F
    :param F: sorted and filtered list F
    :param output_file: filename of index
    :return: index
    """
    index = {}
    for element in F:
        if element[0] in index.keys():
            old_postings_list = index[element[0]]
            if isinstance(old_postings_list, int):
                old_postings_list = [old_postings_list]
            old_postings_list.append(element[1])
            index[element[0]] = old_postings_list  # update postings list
        else:
            index[element[0]] = [element[1]]  # add term and postings list
    output_dic(index, output_file)
    return index

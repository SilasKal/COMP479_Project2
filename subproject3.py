import nltk

from helper_functions import diff_percent, read_index, output_dic


def filter_numbers(index_filename='index_uncompressed.txt', output_filename='index_number.txt'):
    """
    filters out numbers in a given index
    :param index_filename: filename of index that should be filtered
    :param output_filename: filename of compressed index
    :return: filtered index, size of filtered dictionary, difference of filtered dictionary size compared to size
    of original dictionary in percent, size of filtered posting lists, difference of filtered postings lists size
     compared to size of original postings lists in percent
    """
    index = read_index(index_filename)
    filtered_index = {key: value for key, value in index.items() if
                      any(c.isalpha() for c in key) or not any(c.isnumeric() for c in key)}
    len_postings = sum([len(_) for _ in filtered_index.values()])
    output_dic(filtered_index, output_filename)
    return filtered_index, len(filtered_index), diff_percent(len(index), len(filtered_index)), \
           len_postings, diff_percent(sum([len(value) for value in index.values()]), len_postings)


def filter_casefolding(index_filename='index_number.txt', output_filename='index_casef.txt'):
    """
    performs case folding on given index
    :param index_filename: orignal index
    :param output_filename: filename of compressed index
    :return: filtered index, size of filtered dictionary, difference of filtered dictionary size compared to size
    of original dictionary in percent, size of filtered posting lists, difference of filtered postings lists size
     compared to size of original postings lists in percent
    """
    index = read_index(index_filename)
    len_postings_org = sum(len(p) for p in index.values())
    casef_index = {}
    for term, ps in index.items():
        lower_case_word = term.lower()
        if lower_case_word in casef_index.keys():  # if lowercase word already in new index
            casef_index[lower_case_word].extend(ps)
            casef_index[lower_case_word] = sorted(list(set(casef_index[lower_case_word])),
                                                  key=int)  # update postings list
        else:
            casef_index[lower_case_word] = ps  # add postings list
    len_postings_new = sum([len(_) for _ in casef_index.values()])
    output_dic(casef_index, output_filename)
    return casef_index, len(casef_index), diff_percent(len(index), len(casef_index)), len_postings_new, \
           diff_percent(len_postings_org, len_postings_new)


def filter_stop_words(index_filename, output_filename, limit):
    """
    filters given number of most frequent words from index
    :param index_filename: filename of original index
    :param limit: number of most frequent words to be filtered out
    :param output_filename: filename of compressed index
    :return: filtered index, size of filtered dictionary, size of filtered posting lists
    """
    index = read_index(index_filename)
    stopwords = []
    sorted_index = sorted(index.items(), key=lambda x: -len(x[1]))  # sort index based on term frequency
    for elem in sorted_index:
        if limit > 0:
            stopwords.append(elem[0])  # get most frequent words
            limit -= 1
        else:
            break
    filtered_index = {key: value for key, value in index.items() if key not in stopwords}  # filter out stop words
    len_postings_new = sum([len(_) for _ in filtered_index.values()])
    output_dic(filtered_index, output_filename)
    # print('stopwords', limit, len_postings,  sum([len(value) for value in index.values()]), diff_percent(sum([len(
    # value) for value in index.values()]), len_postings))
    return filtered_index, len(filtered_index), len_postings_new


def filter_stemming(index_filename='index_stopw2.txt', output_filename='index_stemm.txt'):
    """
    stems all terms in the vocabulary of an index and returns new updated index
    :param index_filename: filename of original index
    :param output_filename: filename of compressed index
    :return: filtered index, size of filtered dictionary, difference of filtered dictionary size compared to size
    of original dictionary in percent, size of filtered posting lists, difference of filtered postings lists size
     compared to size of original postings lists in percent
    """
    index = read_index(index_filename)
    ps = nltk.PorterStemmer()
    stemm_index = {}
    len_postings_org = sum([len(k) for k in index.values()])
    for term, ps_list in index.items():
        stemmed_word = ps.stem(term)
        if stemmed_word in stemm_index.keys():  # if stemmed word already in new index
            stemm_index[stemmed_word].extend(ps_list)
            stemm_index[stemmed_word] = sorted(list(set(stemm_index[stemmed_word])), key=int)  # update postings list
        else:
            stemm_index[stemmed_word] = sorted(ps_list, key=int)
    len_postings_new = sum([len(_) for _ in stemm_index.values()])
    output_dic(stemm_index, output_filename)
    return stemm_index, len(stemm_index), diff_percent(len(index), len(stemm_index)), len_postings_new, \
           diff_percent(len_postings_org, len_postings_new)

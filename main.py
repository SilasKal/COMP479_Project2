from helper_functions import print_table, diff_percent
from subproject1 import naive_indexer, create_index

from subproject2 import get_query_input
from subproject3 import filter_stemming, filter_numbers, filter_casefolding, filter_stop_words


def main():
    """
    implements the creation of the index and the compression of it
    """
    F = naive_indexer()
    unfiltered_index = create_index(F)
    len_val_unfiltered = sum(len(v) for v in unfiltered_index.values())
    len_unfiltered = len(unfiltered_index)
    index_number, len_number_compr, diff_number_comp, len_number_val, diff_number_val = filter_numbers()
    index_casef, len_casefolding_compr, diff_casefolding_comp, len_casefolding_val, \
        diff_casefolding_val = filter_casefolding()
    index_stopw1, len_stopwords1_compr, len_stopwords1_val = filter_stop_words(
        'index_casef.txt', 'index_stopw1.txt', 30)
    index_stopw2, len_stopword2_compr, len_stopwords2_val = filter_stop_words(
        'index_stopw1.txt', 'index_stopw2.txt', 120)
    index_stemm, len_stemm_compr, diff_stemm_comp, len_stemm_val, diff_stemm_val = filter_stemming()
    print_table(
        ['compression', 'dictionary size', 'difference in percent', 'cml', 'postings lists size', 'difference in '
                                                                                                  'percent',
         'cml'], [['unfiltered', len_unfiltered, 0, 0, len_val_unfiltered, 0, 0],
                  ['no numbers', len_number_compr,
                   diff_number_comp, diff_number_comp, len_number_val, diff_number_val, diff_number_val],
                  ['case folding', len_casefolding_compr,
                   diff_casefolding_comp, diff_percent(len_unfiltered, len_casefolding_compr), len_casefolding_val,
                   diff_casefolding_val, diff_percent(len_val_unfiltered, len_casefolding_val)],
                  ['30 stopw\'s', len_stopwords1_compr,
                   diff_percent(len_casefolding_compr, len_stopwords1_compr),
                   diff_percent(len_unfiltered, len_stopwords1_compr), len_stopwords1_val,
                   diff_percent(len_casefolding_val, len_stopwords1_val),
                   diff_percent(len_val_unfiltered, len_stopwords1_val)],
                  ['150 stopw\'s', len_stopword2_compr,
                   diff_percent(len_casefolding_compr, len_stopword2_compr),
                   diff_percent(len_unfiltered, len_stopword2_compr), len_stopwords2_val,
                   diff_percent(len_casefolding_val, len_stopwords2_val),
                   diff_percent(len_val_unfiltered, len_stopwords2_val)],
                  ['stemming', len_stemm_compr,
                   diff_stemm_comp, diff_percent(len_unfiltered, len_stemm_compr), len_stemm_val, diff_stemm_val,
                   diff_percent(len_val_unfiltered, len_stemm_val)]])


main()
get_query_input()

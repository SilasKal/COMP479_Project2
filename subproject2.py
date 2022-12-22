from helper_functions import read_index


def query_processor(term, index_filename):
    """
    returns the list of documentsID in which the single term can be found in
    :param term: single term
    :param index_filename: filename of index which should be used for the query
    :return: list of documentIDs in which the term can be found in
    """
    index = read_index(index_filename)
    if term in index.keys():
        postings_list = index[term]
        print(len(postings_list), 'documents contain the term \'' + term + '\':', postings_list)
        return index[term]
    else:
        print('No document contains the term \'' + term + '\'.')
        return ''


def test_query():
    """runs sample and tests queries on both indices"""
    print('SAMPLE QUERIES FROM MOODLE:')
    for term in ['copper', 'Samjens', 'Carmark', 'Bundesbank']:
        print('uncompressed Index: ')
        query_processor(term, 'index_uncompressed.txt')
        print('compressed index: ')
        query_processor(term, 'index_stemm.txt')
    print('MY QUERIES AND ADDITIONAL TESTING:')
    for term in ['in', 'article', 'zone', '275', 'Wednesday']:
        print('uncompressed Index: ')
        query_processor(term, 'index_uncompressed.txt')
        print('compressed index: ')
        query_processor(term, 'index_stemm.txt')


def get_query_input():
    """
    implements query search in console
    """
    print('started query processor')
    user_input = input('Type u for searching in the uncompressed index, c for searching in the compressed index, '
                       't for running the tests queries and stop for ending the query \n')
    while user_input not in ['u', 'c', 'stop', 't']:
        print('You mistyped. Try again. ')
        user_input = input(
            'Type u for searching in the uncompressed index, c for searching in the compressed index, t for running '
            'the test queries and stop for ending the query \n')
    else:
        if user_input == 'stop':
            pass
        elif user_input == 't':
            test_query()
            get_query_input()
        else:
            user_input2 = input('Enter the term you want to search for. ')
            if user_input == 'c':
                query_processor(user_input2, 'index_stemm.txt')
                get_query_input()
            elif user_input == 'u':
                query_processor(user_input2, 'index_uncompressed.txt')
                get_query_input()

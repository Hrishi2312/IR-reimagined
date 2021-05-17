from .words import *
from .Node import *

connecting_words = []
cnt = 1
different_words = []
total_files = len(files_with_index)
zeroes_and_ones = []
zeroes_and_ones_of_all_words = []
query_words = []
files = []

def processing(query):
    connecting_words = []
    cnt = 1
    different_words = []
    total_files = len(files_with_index)
    zeroes_and_ones = []
    zeroes_and_ones_of_all_words = []
    query_words = []
    files = []
    query = word_tokenize(query)
    for word in query:
        if word.lower() != "and" and word.lower() != "or" and word.lower() != "not":
            different_words.append(word.lower())
        else:
            connecting_words.append(word.lower())
    for word in (different_words):
        if word.lower() in unique_words_all:
            zeroes_and_ones = [0] * total_files
            linkedlist = linked_list_data[word].head
            query_words.append(word)
            while linkedlist.nextval is not None:
                zeroes_and_ones[linkedlist.nextval.doc - 1] = 1
                linkedlist = linkedlist.nextval
            zeroes_and_ones_of_all_words.append(zeroes_and_ones)
    for word in connecting_words:
        word_list1 = zeroes_and_ones_of_all_words[0]
        word_list2 = zeroes_and_ones_of_all_words[1]
        if word == "and":
            bitwise_op = [w1 & w2 for (w1,w2) in zip(word_list1,word_list2)]
            zeroes_and_ones_of_all_words.remove(word_list1)
            zeroes_and_ones_of_all_words.remove(word_list2)
            zeroes_and_ones_of_all_words.insert(0, bitwise_op);
        elif word == "or":
            bitwise_op = [w1 | w2 for (w1,w2) in zip(word_list1,word_list2)]
            zeroes_and_ones_of_all_words.remove(word_list1)
            zeroes_and_ones_of_all_words.remove(word_list2)
            zeroes_and_ones_of_all_words.insert(0, bitwise_op);
        elif word == "not":
            bitwise_op = [not w1 for w1 in word_list2]
            bitwise_op = [int(b == True) for b in bitwise_op]
            zeroes_and_ones_of_all_words.remove(word_list2)
            zeroes_and_ones_of_all_words.remove(word_list1)
            bitwise_op = [w1 & w2 for (w1,w2) in zip(word_list1,bitwise_op)]
        zeroes_and_ones_of_all_words.insert(0, bitwise_op);

    lis = zeroes_and_ones_of_all_words[0]
    cnt = 1
    for index in lis:
        if index == 1:
            files.append(files_with_index[cnt])
        cnt = cnt+1

    return [query, query_words, connecting_words, zeroes_and_ones_of_all_words, files]

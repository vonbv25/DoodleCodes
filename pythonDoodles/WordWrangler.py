"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    deduplicated_list =[]
    prev_element = None
    for element in list1:
        if element!=prev_element:
            prev_element = element
            deduplicated_list.append(element)

    return deduplicated_list
    

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """  
    return [value for value in list1 if value in list2]

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """
    result = []
    idx = 0
    idx2 = 0
    while idx<len(list1) and idx2<len(list2):
        
        if list1[idx]>=list2[idx2]:
            result.append(list2[idx2])
            idx2+=1
        else:
            result.append(list1[idx])
            idx+=1            
     
    if len(list1)>0:
        result.extend(list1[idx:])
    if len(list2)>0:
        result.extend(list2[idx2:]) 
    return result
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    result = []
    if len(list1) <= 1:
        return list1
    else:
        midpoint = len(list1)/2 
        left = merge_sort(list1[:midpoint])
        right = merge_sort(list1[midpoint:])
        result = merge(left,right)

    return result

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    strings = []
    if len(word)==0:
        return [""]   
    else:
        first = word[0]
        rest = word[1:]
        rest_strings = list(gen_all_strings(rest))
        for string in rest_strings:
            strings.append(string)
            for index in range(0,len(string)+1):
                new_word = string[:index] + first + string[index:]
                strings.append(new_word)
                
    return strings
# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    url = codeskulptor.file2url(filename)
    netfile = urllib2.urlopen(url)    
    data = netfile.read()
    return data

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
run()

    
    

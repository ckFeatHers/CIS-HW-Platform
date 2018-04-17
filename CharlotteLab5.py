#Program 5 PYTHON Charlotte Feathers
#due 17 April 18

def main():
    choice = 1

    words1 = open_words_one()
    words2 = open_words_two()


#open with title and menu    
    print('***********  Python Program 5  *******************')

    while choice != 6:
        menu()
        choice = int(input('Which would you like?  '))
        print()

        if choice == 1:
            unique_words(words1, words2)
           
        elif choice == 2:
            inclusive_words(words1, words2)
            
        elif choice == 3:
            diff1_from2(words1, words2)
            
        elif choice == 4:
            diff2_from1(words1, words2)

        elif choice == 5:
            unique_both(words1, words2)
                        
        elif choice == 6:
            print('Good bye')
            
        else:
            print('Please enter between 1 and 6.')


def menu():          
    print('Enter 1 to display the unique words.')
    print('Enter 2 to display the words that appear in both files.')
    print('Enter 3 to display the words that only appear in the first file.')
    print('Enter 4 to display the words that only appear in the second file.')
    print('Enter 5 to display the unique words in either the file but NOT both.')
    print('Enter 6 to exit the program:')

def open_words_one():
#retrieve the words from both files for manipulation
    input_file1 = input('Enter the name of the input file:  ')
    input_file1 = open(input_file1, 'r')
    input_text1 = input_file1.read()
    text1_lower = input_text1.lower()
    words1_all = text1_lower.split()
    words1 = set(words1_all)
    #got set so can close file1
    input_file1.close()
    return words1

def open_words_two():
    input_file2 = input('Enter the name of the second input file: ')
    input_file2 = open(input_file2, 'r')
    input_text2 = input_file2.read()
    text2_lower = input_text2.lower()
    words2_all = text2_lower.split()
    words2 = set(words2_all)
    input_file2.close()
    return words2

def unique_words(w1, w2):
    print('\nThe unique words found in the two different files:')
    for word in w1:
        print(word)
    for word in w2:
        print(word)
    print()

def inclusive_words(w1, w2):
    inclusive = w1.intersection(w2)
    print('Words that appear in both files are:')
    for item in inclusive:
        print(item)
    print()

def diff1_from2(w1, w2):            
    difference1_2 = w1.difference(w2)
    print('Words in the first file but not found in the second file:')
    for item in difference1_2:
        print(item)
    print()
            
def diff2_from1(w1, w2):            
    difference2_1 = w2.difference(w1)
    print('Words in second file but not found in the first file:')
    for item in difference2_1:
        print(item)
    print()

def unique_both(w1, w2):
    unique_not_both = w1.symmetric_difference(w2)
    print('Unique words in each file but not found in both:')
    for item in unique_not_both:
        print(item)
    print()

main()

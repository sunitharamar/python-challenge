# 
# create a Python script to automate the analysis of any such passage using these metrics. 
# script will need to do the following:
#
# Import a text file filled with a paragraph of your choosing.
# Assess the passage for each of the following:
# Approximate word count
# Approximate sentence count
# Approximate letter count(per word)
# Average sentence length (in words)
#
#
# Import Modules
import re
import os

# Goal - pull out code into seperate functions

def main():

    my_data = [] # initialize the input files list
    words_len = 0 # Approximate word count
    sentence_count = 0 # sentence count
    avg_letter_count = 0 # average letter count
    avg_sentence_len = 0 # average sentence length
    total_letter_count = 0 # total letter count


    # Set path for input and output file
    infile = os.path.join('Resources', 'passage.txt')
    outputf = os.path.join('Resources', 'pyParagraph_analysis.txt')

    word_count = [] # word_count is an array of list

    my_data = [ infile ]  # list with input dataset files
    
    # Loop through all the input dataset files
    for i, infile in enumerate(my_data):


        # Open the txt  file one at a time Hint : indexing of enumerate starts from 0
        with open(infile , 'r') as in_txtfile:

            paragraph_str = in_txtfile.readline()
    
            # This is the splitting of the paragraph into sentences with regular expressions
            sentences = re.split("(?<=[.!?]) +", paragraph_str)
    
            # This is the loop for sentences iteration
            #for sentence in sentences:
                #print(sentence)

            sentence_count = len(sentences)
    
            words = paragraph_str.split()
            words_len = len(words)

        
            
            # Finding all the letters in a word to get the average letter count and average sentence length
            for word in words:

                # Prunning the word with ONLY letters   
                pruned_word  = " ".join(re.findall("[a-zA-Z]+", word))

                # This is another method for finding all letters in a string
                #pruned_word = ""
                #for letter in letters:
                    #if letter.isalpha():
                        #pruned_word += letter
    
                total_letter_count += len(pruned_word) # total letters count from all pruned strings

                avg_letter_count = total_letter_count/words_len # Average letter count
                avg_sentence_len = words_len/sentence_count #Average sentence length
    

    
    # Open a file for writing and create - if it does not exist
    fw = open(outputf, 'a+')

    fw.write("\n\n")
    fw.write("Input file path:  %s\n" %(infile))
        
    #write the header to the outputfile
    fw.write("\n")
    fw.write("\n")
    fw.write("Paragraph Analysis\n")
    fw.write("---------------------------\n")
    fw.write("Approximate Word Count:   %d\n" %(words_len))
    fw.write("Approximate Sentence Count:  %d\n" %(sentence_count))
    fw.write("Average Letter Count:   %11f\n" %(avg_letter_count))
    fw.write("Average Sentence Length: %4.1f \n" %(avg_sentence_len))
    fw.write("\n")
    fw.write("\n")


    fw.close()

if __name__ == "__main__":
    main()
__author__ = 'dhs'

"""This program counts the number of times each unique word appears in
a text file. The results are output to the command line, and the user
is given the option of printing the results to a new text file."""

import os
from shutil import copyfile

COMMON_WORDS = {"the", "be", "are", "is", "were", "was", "am",
                "been", "being", "to", "of", "and", "a", "in",
                "that", "have", "had", "has", "having", "for",
                "not", "on", "with", "as", "do", "does", "did",
                "doing", "done", "at", "but", "by", "from"}

class WordProcess:
    """This class returns the number of times each word appears in a text file."""

    def __init__(self, file):
        """Construct class instance with file attribute"""
        self.file = file

    def sort_by_value(item):
        return item[-1]

    def words_dict(self):
        """Compare user input text file to English wordlist and return matches"""
        if os.path.getsize(self.file) > 1e7:
            return False
        else:
            open_input_file = open(self.file, "r")
            wordlist_path = os.path.expanduser("./wordsEn.txt")
            open_wordlist_file = open(wordlist_path, "r")

            read_input = open_input_file.read().split()
            read_wordlist = open_wordlist_file.read().split()

            count = 0

            for word in read_input:
                word = word.lower()
                read_input[count] = word.strip(".,!\"\';:()")
                count += 1

            word_count = {}

            for word in read_input:
                word = word.lower()
                if word in read_wordlist:
                    if word not in word_count:
                        word_count[word] = 1
                    else:
                        word_count[word] += 1
                else:
                    continue

        open_input_file.close()
        open_wordlist_file.close()

        return word_count

    def print_top_words(self, choice):
        """
        Sort and print each unique word with its frequency to the console.
        Return the results as a list to use in file output
        """
        word_count = self.words_dict()
        # Uses reverse order to sort (most frequent first).
        items = sorted(word_count.items(), key=WordProcess.sort_by_value, reverse=True)
        results_list = []

        # Truncate output if user wants to suppress common words.
        for word in items[:50]:
            if choice == "y" and word[0] not in COMMON_WORDS:
                result = word[0] + ": " + str(word[1]) + " times"
                results_list.append(result)
                print(result)
            elif choice == "n":
                result = word[0] + ": " + str(word[1]) + " times"
                results_list.append(result)
                print(result)

        return results_list

print("Welcome to the F&A text analysis program.\n")

while True:
    user_input = input("Please enter the path and name of the text file you want"
                       "to analyze. (E.g.: C:/Users/Monty/Desktop/file.txt):"
                       "\n")

    print("Reading file, one moment...")

    class_init = WordProcess(user_input)

    if os.path.isfile(user_input) is False:
        print("The file you specified does not exists.\n")
        continue
    else:
        common_word = ""

        print("File read successfully!")

        while common_word != "y" or common_word != "n":
            common_word = input("Would you like to strip common words from the results? "
                                "(Y/N) ").lower()

            if common_word == "y" or common_word == "n":
                break

        print("Compiling results, one moment...\n")

        new_result = WordProcess.print_top_words(class_init, common_word)

        user_output = ""
        while user_output != "y" and user_output != "n":
            user_output = input("\nWould you like to output these results to a file?"
                                "(Y/N) ").lower()

            if user_output == "y":
                # Relative path to current user's desktop.
                user_desktop = os.path.expanduser("~/Desktop")
                output_folder = "/Wordcount Output"

                # Create directory if it doesn't already exist.
                if os.path.isdir(user_desktop + output_folder) is False:
                    os.mkdir(user_desktop + output_folder)

                os.chdir(user_desktop + output_folder)

                # Removes path from file name.
                file_name = user_input.split("/")[-1]
                # Removes file extension from name.
                no_ext = file_name.rsplit(".", 1)[0]

                write_file = open(no_ext + "_results.txt", "w")
                write_file.write("Results for {}:\n\n".format(file_name))

                for line in new_result:
                    write_file.write(line + "\n")

                write_file.close()

                print("Success!")

                copyfile(no_ext + "_results.txt", no_ext + "_results_backup.txt")
                print("Backup file created!\n")

                print("The output folder contains:\n")
                i = 0

                for item in os.listdir():
                    print(os.listdir()[i])
                    i += 1

                break
            elif user_output == "n":
                print("Exiting...")
                break
        break

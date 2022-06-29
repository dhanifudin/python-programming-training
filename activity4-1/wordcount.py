__author__ = 'dhs'

"""This program counts the number of times each unique word appears in
a text file. The results are output to the command line, and the user
is given the option of printing the results to a new text file."""

COMMON_WORDS = {"the", "be", "are", "is", "were", "was", "am",
                "been", "being", "to", "of", "and", "a", "in",
                "that", "have", "had", "has", "having", "for",
                "not", "on", "with", "as", "do", "does", "did",
                "doing", "done", "at", "but", "by", "from"}

user_input = input("Please enter the path and name of the text file you want"
    "to analyze. (E.g.: C:/Users/Monty/Desktop/file.txt):"
    "\n").lower()

if user_input is False:
  print("The file you specified does not exists.\n")
else:
  common_word = input("Would you like to strip common words from the results? "
      "(Y/N) ").lower()

  if common_word == "y" or common_word == "n":
    pass

  user_output = input("\nWould you like to output these results to a file?"
      "(Y/N) ").lower()

  if user_output == "y":
    print("Success!")
  elif user_output == "n":
    print("Exiting...")

# CS15L_LabActivity2_Readability
Simple program to determine reading levels for children

---

### Explain the overall design of your program and justify why you chose this particular class structure and set of user-defined methods.
  The program is a simple readability level determiner. It's a system designed to grade the sentences you've written in automation. The reason why I made this program is to get a glimpse of how determining your readability level works and why you get the level you got. The code consists of an Object-Oriented Programming called Encapsulation. The methods used in this program are main(), __init__(), count_letter(), count_words(), count_sentences().
  
### Describe how user input is handled in your program and discuss the role of exception handling (try–except) in preventing incorrect or unexpected behavior.
  The user input only asks for a word, a letter, a sentence, and basic symbols to get it graded by the program. The exception handling in this code only handles the user input and if there are any possible anomalies are to be handled.

### Identify one limitation of your current implementation and explain how it could be improved using additional OOP concepts or better error handling.
  The one limitation of my program is it doesn't check for the actual grammar of the program. It checks for how the sentence is structured. It could be improved further by implementing a more robust AI grammar checker and start grading it from there.

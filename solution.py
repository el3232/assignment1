# welcome_assignment_answers
# Input - All eight questions given in the assignment.
# Output - The right answer for the specific question.

# attempting to commit to github again


def welcome_assignment_answers(question):
    # The student doesn't have to follow the skeleton for this assignment.
    # Another way to implement is using a "case" statements similar to C.
    # answer = "Please enter one of the 8 questions from 'Computer Networking Assignment 1'"

    # question 1
    answer = None
    if question == "Are encoding and encryption the same? - Yes/No":
        answer = "no"

    # question 2
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "no"
        #  - while legitimate decryption requires a key, breaking " \
        # "encryption is possible by methods such as brute force or rainbow " \
        # "tables, and is technically possible though depending on how much data" \
        # "and what methods were used to encrypt it, might be impractical

    # question 3
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"

    # question 4
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"

    # question 5
    elif question == "What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 " \
                     "hash generator and use the answer in your code":
        answer = "42b76fe51778764973077a5a94056724"

    # question 6
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"

    # question 7
    elif question == "What layer from the TCP/IP model the protocol DHCP belongs to?" \
                     " - The answer should be a numeric number":
        answer = 5

    # question 8
    elif question == "What layer of the TCP/IP model the protocol TCP belongs to?" \
                     " - The answer should be a numeric number":
        answer = 4
    return answer


if __name__ == "__main__":
    # use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No"
    debug_question2 = "Is it possible to decrypt a message without a key? - Yes/No"
    debug_question3 = "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a " \
                      "numeric number"
    debug_question4 = ""
    print(welcome_assignment_answers(debug_question3))

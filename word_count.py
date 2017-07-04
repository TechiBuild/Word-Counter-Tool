import pylab as plt
import operator
import re


def read_text_file():
    path = input("Please enter text file location\n")
    f = open(path, 'r')
    text = f.read()

    return text.upper()


def get_word_count(text):
    word_dict = {}
    default_value = 1
    processed_words_value = 0

    for word in text.split():
        # match a single char that is not in the brackets with \w = [A-Za-z0-9_] and \s = [ \t\r\n\v\f] for
        # tab, carriage return, newline, escape character and form feed.

        word_update = re.sub(r'[^\w\s]', '', word)

        processed_words_value += 1

        if word_update in word_dict:
            value = (1 + word_dict.get(word_update))
            word_dict.update({word_update: value})
        else:
            word_dict.update({word_update: default_value})

    print("Processed Words: " + str(processed_words_value))

    return word_dict


def plot_top_10():
    sorted_ten_list = sort_values()[:10]

    words = [word[0] for word in sorted_ten_list]
    values = [value[1] for value in sorted_ten_list]
    bars = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    plot_data(bars, values, words)


def plot_data(bars, values, words):
    try:
        plt.figure(figsize=(15, 8))
        plt.bar(bars, values)
        plt.xticks(bars, words)
        plt.ylabel('Number of words')
        plt.title('Top 10 words in processed text')
        plt.xlabel('Words')
        plt.show()
    except ValueError:
        print("Error in plotting due to low text input")


def sort_values():
    unsorted_dict = get_word_count(read_text_file())
    sorted_dict = (sorted(unsorted_dict.items(), key=operator.itemgetter(1))[::-1])

    return sorted_dict


if __name__ == '__main__':
    plot_top_10()

def reducer():
    current_word = None
    current_count = 0
    for line in sys.stdin:
        word, count = line.strip().split('\t')
        count = int(count)
        if current_word == word:
            current_count += count
        else:
            if current_word:
                print(current_word + '\t' + str(current_count))
            current_word = word
            current_count = count
    if current_word == word:
        print(current_word + '\t' + str(current_count))

# Main function
if __name__ == '__main__':
    for line in sys.stdin:
        mapper(line)
    reducer()
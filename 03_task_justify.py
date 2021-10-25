words = "Hey there mate, it’s nice to finally meet you!"
maximum_width = 16


"""
The following function justifies the text.
Please pass the text and the maximum width of a line.
"""
def justify(words, max_width):

    lines = []
    words = words.split()

    # split sentence to separate lines of maximum width
    def split_lines(words):
        
        current_line = []
        current_line_lenght = 0
        for word in words:
            current_line.append(word)
            for w in current_line:
                current_line_lenght += len(w)
            if(current_line_lenght >= max_width):
                current_line_lenght -= len(word)
                # current_line.remove(word)
                break
        return current_line
    
    while(len(words)>0):
        line = split_lines(words)
        lines.append(line)
        for w in line:
            if w in words:
                words.remove(w)

    # compute amount of required spaces
    def count_spaces():
        number_of_spaces = []
        for line in lines:
            total_chars = 0
            for word in line:
                total_chars += len(word)
            spaces = max_width - total_chars
            number_of_spaces.append(spaces)
        return number_of_spaces
        # print(number_of_spaces)

        
    # print(count_spaces())
    number_of_spaces = count_spaces()

    new_lines = []

    # add spaces between words
    def add_spaces():
        for line, spaces in zip(lines, number_of_spaces):
            # new_line = " ".join(line)
            # new_lines.append(new_line)
            sp_num = int(round(spaces/len(line)))
            brk = " " * (sp_num + 1)
            # print(type(spaces))
            new_line = brk.join(line)
            new_lines.append(new_line)

        new_lines.remove(new_lines[-1])
        new_lines.append(lines[-1][0])
        return new_lines

    # return the result
    return add_spaces()

justified = justify(words, 16)
# print(words + "\n\n")
# print(justified)
for line in justified:
    print(line)
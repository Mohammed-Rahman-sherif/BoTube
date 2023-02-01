def format_text(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    new_lines = []
    for line in lines:
        words = line.split()
        line_length = len(words)
        if line_length > 7:
            current_line = []
            for word in words:
                current_line.append(word)
                if len(current_line) == 7:
                    new_lines.append(' '.join(current_line))
                    current_line = []
            if current_line:
                new_lines.append(' '.join(current_line))
        elif line_length < 7:
            current_line = words
            for i in range(len(lines) - 1):
                next_line = lines[i + 1].split()
                if len(current_line + next_line) <= 7:
                    current_line += next_line
                else:
                    new_lines.append(' '.join(current_line))
                    break
            else:
                new_lines.append(' '.join(current_line))
        else:
            new_lines.append(line.strip())
    with open(filename, "w") as file:
        file.write('\n'.join(new_lines))


format_text('../Contents/wKXfq.txt')
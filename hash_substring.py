# python3
B = 13
Q = 256
def read_input():
    if input() == 'i':
        return (input().rstrip(), input().rstrip())
    else:
        with open("test/06") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
            return (pattern, text)
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
def get_hash(pattern: str) -> int:
    global B, Q
    m = len(pattern)
    result = 0 
    for i in range(m):
        result = (result * B + ord(pattern[i])) % Q
    return result
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
   

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    pattern_len = len(pattern)
    main_text_len = len(text)

    multiplier = 1
    for i in range(1, pattern_len):
        multiplier = (multiplier * B) % Q

    pattern_hash = get_hash(pattern)
    text_hash = get_hash(text[:pattern_len])

    result = []

    for i in range(main_text_len - pattern_len + 1):
        if pattern_hash == text_hash:
            if text[i:i+pattern_len] == pattern:
                result.append(i)
        if i < main_text_len - pattern_len:
            text_hash = (text_hash - ord(text[i]) * multiplier) * B + ord(text[i + pattern_len])
            if text_hash < 0:
                text_hash += Q
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    return result


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))


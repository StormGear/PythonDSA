# This was asked by Micro1, I believe it's some kind of job search platform.

def text_message(message: str, max_length: int) -> list:
    res = []
    if not message:
        return res
    
    words = message.split()
    n = len(words)
    i = 0
    while i < n:
        line = ''
        while i < n and len(line) + len(words[i]) <= max_length:
            line += words[i] + ' '
            i += 1
        res.append(line.strip())

    return res

if __name__ == '__main__':
    message = "The quick brown fox jumps"
    max_length = 10
    print(text_message(message, max_length))  # Output: ['Hello, how', 'are you', 'doing', 'today?']
    

# Simple Word Ladder implementation using BFS

from collections import deque

def word_ladder(begin, end, word_list):
    word_set = set(word_list)
    queue = deque([(begin, 1)])
    while queue:
        word, steps = queue.popleft()
        if word == end:
            return steps
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in word_set:
                    word_set.remove(next_word)
                    queue.append((next_word, steps + 1))
    return 0

begin_word = "hit"
end_word = "cog"
dictionary = ["hot","dot","dog","lot","log","cog"]

print("Shortest Transformation Length:", word_ladder(begin_word, end_word, dictionary))

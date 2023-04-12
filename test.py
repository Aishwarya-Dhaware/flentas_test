

#Coding Assignment Solution     



from collections import Counter

def check_permutation_exists(pattern, text):
    pattern_count = Counter(pattern)
    window_count = Counter(text[:len(pattern)])
    for i in range(len(pattern), len(text)):
        if pattern_count == window_count:
            return "YES"
        window_count[text[i-len(pattern)]] -= 1
        if window_count[text[i-len(pattern)]] == 0:
            del window_count[text[i-len(pattern)]]
        window_count[text[i]] += 1
    return "YES" if pattern_count == window_count else "NO"

# reading input
T = int(input())
for _ in range(T):
    pattern = input().strip()
    text = input().strip()
    print(check_permutation_exists(pattern, text))


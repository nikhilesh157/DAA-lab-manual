import time
import random
import string


def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    matches = []
    comparisons = 0

    for i in range(n - m + 1):
        j = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            matches.append(i)

    return matches, comparisons


def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    return lps


def kmp_search(text, pattern):
    n, m = len(text), len(pattern)

    if m == 0:
        return [], 0

    lps = compute_lps(pattern)
    matches = []
    comparisons = 0

    i = j = 0

    while i < n:
        comparisons += 1

        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            matches.append(i - j)
            j = lps[j - 1]

        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches, comparisons


def rabin_karp(text, pattern, q=101):
    n, m = len(text), len(pattern)
    d = 256

    if m == 0 or m > n:
        return [], 0

    h = pow(d, m - 1, q)
    p_hash = 0
    t_hash = 0

    matches = []
    comparisons = 0

    # Initial hash values
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    # Slide the pattern
    for s in range(n - m + 1):

        if p_hash == t_hash:
            for k in range(m):
                comparisons += 1
                if text[s + k] != pattern[k]:
                    break
            else:
                matches.append(s)

        if s < n - m:
            t_hash = (
                d * (t_hash - ord(text[s]) * h) + ord(text[s + m])
            ) % q

            if t_hash < 0:
                t_hash += q

    return matches, comparisons


# ---------------- MAIN ----------------

text = "AABAACAADAABAABA"
pattern = "AABA"

print("Text:", text)
print("Pattern:", pattern)

m1, c1 = naive_search(text, pattern)
m2, c2 = kmp_search(text, pattern)
m3, c3 = rabin_karp(text, pattern)

print(f"\nNaive -> Matches at: {m1}, Comparisons: {c1}")
print(f"KMP   -> Matches at: {m2}, Comparisons: {c2}")
print(f"RK    -> Matches at: {m3}, Comparisons: {c3}")

text_large = ''.join(random.choices("ABCD", k=10000))
patterns = ["AB", "ABCD", "ABCDAB", "ABCDABCD"]

print(f"\n{'Pattern':>12} {'Naive':>12} {'KMP':>12} {'RK':>12}")
print("-" * 52)

for p in patterns:
    _, c1 = naive_search(text_large, p)
    _, c2 = kmp_search(text_large, p)
    _, c3 = rabin_karp(text_large, p)

    print(f"{p:>12} {c1:>12} {c2:>12} {c3:>12}")
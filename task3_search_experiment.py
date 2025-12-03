import timeit

def kmp_search(text, pattern):
    lps = [0] * len(pattern)
    j = 0  #index for pattern

    def compute_lps():
        length = 0  
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length-1]
                else:
                    lps[i] = 0
                    i += 1

    compute_lps()

    i = 0  #index for text
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j  
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return -1


def rabin_karp_search(text, pattern, base=256, mod=101):
    m, n = len(pattern), len(text)
    if m > n:
        return -1

    hpattern = 0
    htext = 0
    h = 1  

    for i in range(m-1):
        h = (h * base) % mod

    for i in range(m):
        hpattern = (base * hpattern + ord(pattern[i])) % mod
        htext = (base * htext + ord(text[i])) % mod

    for i in range(n - m + 1):
        if hpattern == htext:
            if text[i:i+m] == pattern:
                return i
        if i < n - m:
            htext = (htext - h * ord(text[i])) % mod
            htext = (htext * base + ord(text[i + m])) % mod
            htext = (htext + mod) % mod
    return -1


def boyer_moore_search(text, pattern):
    def build_last_occurrence():
        last = {}
        for i in range(len(pattern)):
            last[pattern[i]] = i
        return last

    last = build_last_occurrence()
    m, n = len(pattern), len(text)
    i = m - 1
    j = m - 1

    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            lo = last.get(text[i], -1)
            i += m - min(j, 1 + lo)
            j = m - 1
    return -1

# Measuring the running time of algorithms
def measure_time(search_func, text, pattern, repeats=10):
    def wrapper():
        search_func(text, pattern)
    return timeit.timeit(wrapper, number=repeats) / repeats

with open("стаття1.txt", "r", encoding="utf-8") as f:
    text1 = f.read()

with open("стаття2.txt", "r", encoding="utf-8") as f:
    text2 = f.read()

# Choosing a real and fake substring
real_substring_1 = "виклики"
fake_substring_1 = "користуючись"  

real_substring_2 = "експеримент" 
fake_substring_2 = "індекс"   

search_algorithms = {
    "KMP": kmp_search,
    "Rabin-Karp": rabin_karp_search,
    "Boyer-Moore": boyer_moore_search
}

results = {}

for text_name, text, real_sub, fake_sub in [
    ("text1", text1, real_substring_1, fake_substring_1),
    ("text2", text2, real_substring_2, fake_substring_2)
]:
    results[text_name] = {}
    for name, func in search_algorithms.items():
        t_real = measure_time(func, text, real_sub)
        t_fake = measure_time(func, text, fake_sub)
        results[text_name][name] = {"real": t_real, "fake": t_fake}

# Output
for text_name in results:
    print(f"Результати для {text_name}:")
    for algo in results[text_name]:
        print(f"  {algo} - реальний підрядок: {results[text_name][algo]['real']:.6f} сек, "
              f"вигаданий підрядок: {results[text_name][algo]['fake']:.6f} сек")
    # Find fastest algorithm
    real_fastest = min(results[text_name].items(), key=lambda x: x[1]['real'])
    fake_fastest = min(results[text_name].items(), key=lambda x: x[1]['fake'])
    print(f"  Найшвидший (реальний): {real_fastest[0]}")
    print(f"  Найшвидший (вигаданий): {fake_fastest[0]}\n")

# Overall fastest by total time for both texts:
totals = {}
for algo in search_algorithms:
    total = 0
    for text_name in results:
        total += results[text_name][algo]['real'] + results[text_name][algo]['fake']
    totals[algo] = total

overall_fastest = min(totals.items(), key=lambda x: x[1])
print(f"Загальний найшвидший алгоритм: {overall_fastest[0]}")

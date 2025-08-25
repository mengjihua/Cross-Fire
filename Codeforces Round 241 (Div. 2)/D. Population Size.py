import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = list(map(int, data[index:index + n]))
        index += n
        
        start = 0
        segments = 0
        while start < n:
            count_non_zero = 0
            first_index = -1
            first_value = -1
            last_index = -1
            last_value = -1
            d = 0
            r = start
            while r < n:
                x = a[r]
                if count_non_zero == 0:
                    if x != -1:
                        count_non_zero = 1
                        first_index = r
                        first_value = x
                        last_index = r
                        last_value = x
                elif count_non_zero == 1:
                    if x != -1:
                        diff_index = r - first_index
                        diff_value = x - first_value
                        if diff_index == 0:
                            break
                        if diff_value % diff_index != 0:
                            break
                        d = diff_value // diff_index
                        v0 = first_value - d * (first_index - start)
                        if v0 < 1:
                            break
                        count_non_zero = 2
                        last_index = r
                        last_value = x
                else:
                    next_val = last_value + d * (r - last_index)
                    if x != -1:
                        if x != next_val:
                            break
                        last_index = r
                        last_value = x
                    else:
                        if next_val < 1:
                            break
                r += 1
            segments += 1
            start = r
        results.append(str(segments))
    print("\n".join(results))

if __name__ == "__main__":
    main()
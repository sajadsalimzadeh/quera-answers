# n = input()
# a = input()

MAX = 1000000000
MIN = -1000000000

n = 8
a = "1 3 -8 3 4 1 -9 7"

n = int(n)
a = list(map(int, a.split(' ')))
notUsed = list(map(bool, range(1, n + 1)))

len_a = len(a)


class Segment:
    def __init__(self, start, end, _sum=MIN):
        self.start_index = start
        self.end_index = end
        self.sum = _sum
        self.count = 0
        self.min_value = MAX
        self.min_index = -1

    def __str__(self) -> str:
        return f"{self.start_index}~{self.end_index} sum: {self.sum}"


used_segments = []
free_segments = [Segment(0, len_a - 1)]


def fragment_free_segment(parent_segment):
    segments = []

    i = parent_segment.start_index
    segment = Segment(i, i, 0)
    pre_ai = a[i]
    while i <= parent_segment.end_index:
        ai = a[i]

        if segment.min_value < ai:
            segment.min_index = i
            segment.min_value = ai

        if segment.sum != 0 and (ai * pre_ai < 0):
            segments.append(segment)
            segment = Segment(i, i, 0)
        else:
            segment.end_index = i

        segment.count += 1
        segment.sum += ai
        pre_ai = ai
        i += 1

    segments.append(segment)

    j = 1
    len_segments = len(segments)
    while j < len_segments - 1:
        if segments[j].sum < 0:
            temp = segments[j - 1].sum + segments[j].sum + segments[j + 1].sum
            if temp > segments[j - 1].sum and temp > segments[j + 1].sum:
                segments[j].sum = temp
                segments[j].count = segments[j - 1].count + segments[j + 1].count
                segments[j].start_index = segments[j - 1].start_index
                segments[j].end_index = segments[j + 1].end_index
                segments.pop(j - 1)
                segments.pop(j)
                len_segments -= 2
                j -= 2
        j += 1

    best = parent_segment
    for item in segments:
        if item.sum > best.sum:
            best = item

    return best


print('')
print(a)


def print_state():
    # return
    print('----------------')
    print('free segments')
    for free_segment in free_segments:
        print(free_segment)

    print('\nused segments')
    for used_segment in used_segments:
        print(used_segment)


print_state()

total_sum = 0
k = 0
while k < 4:
    f = 0
    free_segment_index = 0
    best_segment = None
    for free_segment in free_segments:
        segment = fragment_free_segment(free_segment)
        if best_segment is None or segment.sum > best_segment.sum:
            best_segment = segment
            free_segment_index = f
        f += 1

    min_index = 0
    min_used_segment = None
    i = 0
    len_used = len(used_segments)
    while i < len_used:
        used_segment = used_segments[i]
        if min_used_segment is None or (used_segment.min_value < min_used_segment.min_value and used_segment.end_index - used_segment.start_index > 0 and notUsed[i] == True):
            min_used_segment = used_segment.min_value
            min_index = i
        i += 1

    if min_used_segment is not None or best_segment is None and (min_used_segment.min_value < 0 and abs(min_used_segment.min_value) > best_segment.sum):
        notUsed[i] = False
        total_sum += abs(min_value)
    else:
        total_sum += best_segment.sum
        used_segments.append(best_segment)

        free_segment = free_segments[free_segment_index]

        f1 = Segment(free_segment.start_index, best_segment.start_index - 1)
        f2 = Segment(best_segment.end_index + 1, free_segment.end_index)

        if best_segment.start_index != f1.start_index and best_segment.end_index != f1.end_index:
            free_segments.append(f1)
        if best_segment.start_index != f2.start_index and best_segment.end_index != f2.end_index:
            free_segments.append(f2)

        free_segments.pop(free_segment_index)

    print_state()
    print('total_sum: ', total_sum, f"{best_segment.start_index}~{best_segment.end_index}")
    k += 1

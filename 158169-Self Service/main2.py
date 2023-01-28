# n = input()
# a = input()

MIN = -1000000000

n = 8
a = "1 3 -8 3 4 1 -9 7"

n = int(n)
a = list(map(int, a.split(' ')))
used = list(map(bool, range(1,n + 1)))

len_a = len(a)

class Segment():
    def __init__(self, start, end, sum = MIN):
        self.start_index = start
        self.end_index = end
        self.sum = sum
        
    def __str__(self) -> str:
        return f"{self.start_index}~{self.end_index} sum: {self.sum}"

used_segments = []
free_segments = [Segment(0, len_a - 1)]

def fragment_segment(segment):
    segments = []
    
    _sum = 0
    _max_sum = MIN
    start_index = segment.start_index
    end_index = start_index
    i = start_index
    while i <= segment.end_index:
        ai = a[i]
        
        if(_sum < 0 and ai > 0):
            start_index = i
            end_index = i
            _sum = 0
            
        _sum += ai
        
        if(_sum > _max_sum):
            _max_sum = _sum
            end_index = i
        
        if(_sum < 0):
            segments.append(Segment(start_index, end_index, _max_sum))
            _max_sum = MIN
            _sum = 0
            
        i += 1
    
    best = segment
    for segment in segments:
        if(segment.sum > best.sum):
            best = segment
    
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
while(k < n):
    f = 0
    free_segment_index = 0
    best_segment = Segment(0,0)
    for free_segment in free_segments:
        segment = fragment_segment(free_segment)
        if(segment.sum > best_segment.sum):
            best_segment = segment
            free_segment_index = f
        f += 1

    total_sum += best_segment.sum
    used_segments.append(best_segment)

    free_segment = free_segments[free_segment_index]
    free_segments.append(Segment(free_segment.start_index, best_segment.start_index - 1))
    free_segments.append(Segment(best_segment.end_index + 1, free_segment.end_index))
    free_segments.pop(free_segment_index)

    print_state()
    print('total_sum: ', total_sum, f"{best_segment.start_index}~{best_segment.end_index}")
    k += 1
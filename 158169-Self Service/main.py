n = int(input())
a = list(map(int, input().split(' ')))

class Item:
    def __init__(self):
        self.sum = 0
        self.items = []
    
    def __str__(self):
        return f"{self.sum} : {self.items}"

a_len = len(a)

i = 0
item = Item()
segments = []
is_pre_possetive = a[0] >= 0
while i < a_len:
    ai = a[i]
    is_possetive = ai >= 0
    if i > 0 and (is_possetive != is_pre_possetive or ai < 0):
        item.items.sort(reverse=item.sum > 0)
        segments.append(item)
        item = Item()
        is_pre_possetive = is_possetive
    
    item.sum += ai
    item.items.append(ai)
    i += 1
    
segments.append(item)

seg_len = len(segments)

def ItemSort(item):
    return item.sum

segments.sort(key=ItemSort, reverse=True)

# i = 0
# while i < len(segments):
#     print(segments[i])
#     i += 1

possetive_seg_count = 0
i = 0
while i < seg_len:
    if segments[i].sum < 0: 
        break
    possetive_seg_count += 1
    i += 1

# print('possetive_seg_count', possetive_seg_count)

k = 0
while k < n:
    sum_k = 0
    seg_counter = 0
    person_num = 0
    while seg_counter < seg_len and person_num <= k:
        segment = segments[seg_counter]
        segment_item_len = len(segment.items)
        
        i = 0
        while i < segment_item_len:
            item = segment.items[i]
            if item < 0 and person_num > k:
                break
            sum_k += item
            if (possetive_seg_count - k + person_num) <= 0:
                person_num += 1
            i += 1
        
        if (possetive_seg_count - k + person_num) > 0:
            person_num += 1
        seg_counter += 1
    
    print(sum_k)
    k += 1
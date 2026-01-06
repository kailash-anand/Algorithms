class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        in_heap_map = set()
        result = []

        def pair_sum(item):
            return nums1[item[0]] + nums2[item[1]]

        def get_parent(n):
            if n == 0:
                return -1

            return (n - 1) // 2

        def bubble_up(heap, index):
            parent = get_parent(index)

            if parent != -1:
                if pair_sum(heap[index]) < pair_sum(heap[parent]):
                    tmp = heap[parent]
                    heap[parent] = heap[index]
                    heap[index] = tmp

                    bubble_up(heap, parent)

        def bubble_down(heap, index):
            min_index = index
            left_chld = index * 2 + 1

            for i in range(0, 2):
                if ((left_chld + i) < len(heap)):
                    if pair_sum(heap[left_chld + i]) < pair_sum(heap[min_index]):
                        min_index = left_chld + i

            if min_index != index:
                tmp = heap[index]
                heap[index] = heap[min_index]
                heap[min_index] = tmp
                bubble_down(heap, min_index)

        def insert(heap, val):
            heap.append(val)
            bubble_up(heap, len(heap) - 1)

        def remove(heap):
            val = heap[0]
            heap[0] = heap[len(heap) - 1]
            heap.pop()
            bubble_down(heap, 0)
            return val

        insert(heap, [0, 0])
        in_heap_map.add((0, 0))

        while k > 0 and heap:
            min_indices = remove(heap)
            result.append([nums1[min_indices[0]], nums2[min_indices[1]]])

            new_pair = [min_indices[0] + 1, min_indices[1]] if (min_indices[0] + 1) < len(nums1) else None
            if new_pair and not (new_pair[0], new_pair[1]) in in_heap_map:
                insert(heap, new_pair)
                in_heap_map.add((new_pair[0], new_pair[1]))

            new_pair = [min_indices[0], min_indices[1] + 1] if (min_indices[1] + 1) < len(nums2) else None
            if new_pair and not (new_pair[0], new_pair[1]) in in_heap_map:
                insert(heap, new_pair)
                in_heap_map.add((new_pair[0], new_pair[1]))

            k -= 1

        return result
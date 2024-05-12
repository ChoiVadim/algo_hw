# UID: 2022203502 최바딤
from collections import deque

debug = False


def count_variance(arr: list[tuple]) -> float:
    # Time complexity: O(n)
    # Space complexity: O(n)
    if not arr:
        return

    data = [i[1] for i in arr]

    mean = sum(data) / len(data)
    squared_diff = [(x - mean) ** 2 for x in data]
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff / len(data)

    return variance


def sort_and_divide_list_by_k_groups(arr: list, k: int) -> list:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    sorted_scores = sorted(arr, reverse=True, key=lambda x: x[1])

    group_size = len(sorted_scores) // k
    groups = [
        deque(sorted_scores[i * group_size : (i + 1) * group_size])
        for i in range(k - 1)
    ]
    groups.append(deque(sorted_scores[(k - 1) * group_size :]))

    return groups


def divide_students(scores, k):
    # Time complexity: O(n^2)
    # Space complexity: O(n)
    groups = sort_and_divide_list_by_k_groups(scores, k)
    before_variance = [count_variance(i) for i in groups]
    new_variance = [i for i in before_variance]

    for i in range(k - 1):
        # From right to left
        while True:
            before_var_sum = before_variance[i] + before_variance[i + 1]

            # If in both groups variance is 0, break
            if new_variance[i] == 0 and new_variance[i + 1] == 0:
                break

            # Pop the first element from second group and insert to end of first group
            # If length of second group is greater than 1
            if len(groups[i + 1]) > 1:
                val = groups[i + 1].popleft()
                groups[i].append(val)
            else:
                break

            # Calculate new variance
            new_variance[i] = count_variance(groups[i])
            new_variance[i + 1] = count_variance(groups[i + 1])
            new_var_sum = new_variance[i] + new_variance[i + 1]

            if new_var_sum < before_var_sum or new_variance[i] == 0:
                before_variance[i] = count_variance(groups[i])
                before_variance[i + 1] = count_variance(groups[i + 1])

            else:
                val = groups[i].pop()
                groups[i + 1].appendleft(val)
                break

        # From left to right
        while True:
            before_var_sum = before_variance[i] + before_variance[i + 1]

            if new_variance[i] == 0 and new_variance[i + 1] == 0:
                break

            # Pop the last element from first group and insert to front of second group
            # If length of second group is greater than 1
            if len(groups[i]) > 1:
                val = groups[i].pop()
                groups[i + 1].appendleft(val)
            else:
                break

            # Calculate new variance
            new_variance[i] = count_variance(groups[i])
            new_variance[i + 1] = count_variance(groups[i + 1])
            new_var_sum = new_variance[i] + new_variance[i + 1]

            if new_var_sum < before_var_sum or new_variance[i + 1] == 0:
                before_variance[i] = count_variance(groups[i])
                before_variance[i + 1] = count_variance(groups[i + 1])

            else:
                val = groups[i + 1].popleft()
                groups[i].append(val)
                break

    return groups, round(sum(before_variance), 3)


def main():
    k = int(input("Enter k: "))
    arr = input("Enter array: ").split()
    arr = [(i, int(j)) for i, j in enumerate(arr, 1)]

    if debug:
        print(arr)

    res = divide_students(arr, k)

    print(f"Maximum sum of differences: {res[1]}")

    if debug:
        print(res[0])

    with open("Partition2.txt", "w") as f:
        for group in res[0]:
            f.write(" ".join(f"{i}({j})" for i, j in group) + "\n")


if __name__ == "__main__":
    main()

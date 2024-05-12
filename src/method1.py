# UID: 2022203502 최바딤
debug: bool = False


def find_max_diff(arr: list[list], k: int) -> int:
    # Time complexity: O(n) min, max functions
    # Space complexity: O(1)
    if not arr:
        return

    max_sum: int = 0

    for i in range(0, k - 1):
        min_score = min(arr[i], key=lambda x: x[1])
        max_score = max(arr[i + 1], key=lambda x: x[1])

        if debug:
            print(f"{min_score=}, {max_score=}")

        sum_diff = min_score[1] - max_score[1]

        if debug:
            print(f"{sum_diff=}\n")

        max_sum += sum_diff

    return max_sum


def divide_array(arr: list, k: int) -> list[list]:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    arr.sort(reverse=True, key=lambda x: x[1])

    if debug:
        print(list)

    final_arr: list = []
    temp_arr: list = []
    max_diff: int = 0
    max_diff_index: int = -1

    for i in range(k - 1):
        temp_arr = arr[max_diff_index + 1 :]
        arr_len = len(temp_arr)

        for i in range(0, arr_len - 1):
            diff = temp_arr[i][1] - temp_arr[i + 1][1]

            if diff > max_diff:
                max_diff = diff
                max_diff_index = i

        max_diff = 0
        final_arr.append(temp_arr[: max_diff_index + 1])

    final_arr.append(temp_arr[max_diff_index + 1 :])

    if debug:
        print("\n")
        for i in range(k):
            print(f"{final_arr[i]}")
        print("\n")

    return final_arr


def main():
    k = int(input("Enter k: "))
    arr = input("Enter array: ").split()
    arr = [(i, int(j)) for i, j in enumerate(arr, 1)]

    if debug:
        print(arr)

    final_array = divide_array(arr, k)
    max_sum = str(find_max_diff(final_array, k))

    print(f"Maximum sum of differences: {max_sum}")

    if debug:
        print(final_array)

    with open("Partition1.txt", "w") as f:
        for arr in final_array:
            f.write(" ".join(f"{i}({j})" for i, j in arr) + "\n")


if __name__ == "__main__":
    main()

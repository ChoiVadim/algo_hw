debug = False


def count_variance(arr: list) -> float:
    data = [i[1] for i in arr]

    if data:
        mean = sum(data) / len(data)

        squared_diff = [(x - mean) ** 2 for x in data]

        sum_squared_diff = sum(squared_diff)

        variance = sum_squared_diff / len(data)

        return variance


def sort_and_divide_list_by_k_groups(arr: list, k: int) -> list:
    sorted_scores = sorted(arr, reverse=True, key=lambda x: x[1])

    group_size = len(sorted_scores) // k
    groups = [
        sorted_scores[i * group_size : (i + 1) * group_size] for i in range(k - 1)
    ]
    groups.append(sorted_scores[(k - 1) * group_size :])

    return groups


def divide_students(scores, k):
    groups = sort_and_divide_list_by_k_groups(scores, k)
    before_variance = [count_variance(i) for i in groups]
    new_variance = [count_variance(i) for i in groups]

    for i in range(k - 1):
        while groups[i] and groups[i + 1]:
            before_var_sum = before_variance[i] + before_variance[i + 1]

            if new_variance[i] == 0 and new_variance[i + 1] == 0:
                break

            val = groups[i + 1].pop(0)
            groups[i].append(val)

            # Calculate new variance
            new_variance[i] = count_variance(groups[i])
            new_variance[i + 1] = count_variance(groups[i + 1])

            if new_variance[i + 1] != None:
                new_var_sum = new_variance[i] + new_variance[i + 1]
            else:
                val = groups[i].pop()
                groups[i + 1].insert(0, val)
                break

            if new_var_sum < before_var_sum or new_variance[i] == 0:
                before_variance[i] = count_variance(groups[i])
                before_variance[i + 1] = count_variance(groups[i + 1])
            else:
                val = groups[i].pop()
                groups[i + 1].insert(0, val)
                break

        while groups[i] and groups[i + 1]:
            before_var_sum = before_variance[i] + before_variance[i + 1]

            if new_variance[i] == 0 and new_variance[i + 1] == 0:
                break
            # Pop the last element from first group and insert to front of second group
            val = groups[i].pop()
            groups[i + 1].insert(0, val)

            # Calculate new variance
            new_variance[i] = count_variance(groups[i])
            new_variance[i + 1] = count_variance(groups[i + 1])

            if new_variance[i] != None:
                new_var_sum = new_variance[i] + new_variance[i + 1]
            else:
                val = groups[i + 1].pop(0)
                groups[i].append(val)
                break

            if new_var_sum < before_var_sum or new_variance[i] == 0:
                before_variance[i] = count_variance(groups[i])
                before_variance[i + 1] = count_variance(groups[i + 1])

            else:
                val = groups[i + 1].pop(0)
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
        for arr in res[0]:
            f.write(" ".join(f"{i}({j})" for i, j in arr) + "\n")


if __name__ == "__main__":
    main()

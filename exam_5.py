# exam 5
def divisible_by_5_and_7(low: int = 1500, high: int = 2700) -> list[int]:
    step = 35  # ppcm(5,7)
    start = ((low + step - 1) // step) * step
    return list(range(start, high + 1, step))

if __name__ == "__main__":
    nums = divisible_by_5_and_7()
    print(nums)                     # liste Python
    print(",".join(map(str, nums))) # format séparé par des virgules
from main import *

run_cases = [
    ([7, 4, 3, 100, 2343243, 343434, 1, 2, 32], 1),
    ([12, 12, 12], 12),
    ([10, 200, 3000, 5000, 4], 4),
]

submit_cases = run_cases + [
    ([1], 1),
    ([1, 2, 3, 4, 5], 1),
    ([5, 4, 3, 2, 1], 1),
    ([100, 200, 300, 400, 500], 100),
    ([500, 400, 300, 200, 100], 100),
    ([], None),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    print(f"Expecting: {expected_output}")
    result = find_minimum(input1)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main_find_min():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


run_cases = [([7, 4, 3, 100, 2343243, 343434, 1, 2, 32], 2686826), ([12, 12, 12], 36)]

submit_cases = run_cases + [
    ([10, 200, 3000, 5000, 4], 8214),
    ([], 0),
    ([1], 1),
    ([123456789], 123456789),
    ([-1, -2, -3], -6),
    ([0, 0, 0, 0, 0], 0),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * nums: {input1}")
    print(f"Expecting: {expected_output}")
    result = sum(input1)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main_sum():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")

run_cases = [
    ([7, 4, 3, 100, 765, 2344, 1, 2, 32], 5056),
    ([12, 12, 12], 45),
    ([10, 200, 3000, 5000, 4], 11333),
]

submit_cases = run_cases + [
    ([], 0),
    ([1, 1, 1], 4),
    ([100], 100),
    ([50, 60, 70, 80, 90], 483),
    ([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 872),
    (
        [
            5,
            10,
            15,
            20,
            25,
            30,
            35,
            40,
            45,
            50,
            55,
            60,
            65,
            70,
            75,
            80,
            85,
            90,
            95,
            100,
        ],
        1912,
    ),
]


def test(input1, expected_output):
    try:
        print("---------------------------------")
        print(f"Inputs: {input1}")
        print(f"Expecting: {expected_output}")
        result = round(get_estimated_spread(input1))
        print(f"Actual: {result}")
        if result == expected_output:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print("Fail")
        print(e)
        return False


def main_spread():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")

import time

run_cases = [
    (10, [i for i in range(200)], True),
    (-1, [i for i in range(20000)], False),
]

submit_cases = run_cases + [
    (15, [], False),
    (0, [0], True),
    (-1, [-2, -1], True),
    (105028, [i for i in range(2000000)], True),
    (2000001, [i for i in range(2000000)], False),
]


def test(target, arr, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * target: {target}")
    print(f" * arr length: {len(arr)} items")
    print(f"Expecting: {expected_output} & completed in less than 50 milliseconds")
    start = time.time()
    result = binary_search(target, arr)
    end = time.time()
    timeout = 0.05
    if (end - start) < timeout:
        print(f"binary_search completed in less than {timeout * 1000} milliseconds!")
        if result == expected_output:
            print(f"Actual: {result}")
            print("Pass")
            return True
        else:
            print(f"Actual: {result}")
            print("Fail")
            return False
    else:
        print(
            f"binary_search took too long ({(end - start) * 1000} milliseconds). Speed it up!"
        )
        print(f"Actual: {result}")
        print("Fail")
        return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

import math, time, random

start = time.time()

with open('./input.txt') as f:
    puzzle_input = f.read().split("\n\n")

rules = puzzle_input[0].splitlines()
updates = puzzle_input[1].splitlines()

page_order_rule = {}

def check_update_order(_update:list[str]):
    for i, n in enumerate(_update):
        prev_numbers = _update[0:i + 1]

        if n not in page_order_rule:
            continue

        not_allowed_numbers = page_order_rule[n]

        for prev_number in prev_numbers:
            if prev_number in not_allowed_numbers:
                return False

    return True

def sort_pages(_update):
    page_order = []

    for page in _update:
        if len(page_order) == 0:
            page_order.append(page)
            continue

        numbers_that_must_be_after = page_order_rule[page]
        lowest_index = 1000
        for number_that_must_be_after in numbers_that_must_be_after:
            if number_that_must_be_after in page_order and page_order.index(number_that_must_be_after) < lowest_index:
                lowest_index = page_order.index(number_that_must_be_after)

        if lowest_index == 1000:
            page_order.append(page)
        else:
            page_order.insert(lowest_index, page)

    return page_order


for rule in rules:
    num1, num2 = rule.split('|')

    if num1 in page_order_rule:
        page_order_rule[num1].append(num2)
    else:
        page_order_rule[num1] = [num2]


correct_count = 0
incorrect_count = 0


for index, update in enumerate(updates):
    update_list = update.split(",")
    if check_update_order(update_list):
        correct_count += int(update_list[math.floor(len(update_list) / 2)]) # Part 1
    else:
        incorrect_count += int(sort_pages(update_list)[math.floor(len(update_list) / 2)]) # Part 2


print(correct_count, incorrect_count, round((time.time() - start) * 1000, 3)) # 6.279ms

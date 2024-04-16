# //

card_num = '5610591081018250'

def sum_nums(nums):
  result = 0
  for num in nums:
    result += int(num)
  return result


def add_double_value(nums):
  new_arr = []
  for num in nums:
    if len(num) > 1:
      new_num = sum_nums(num)
      new_arr.append(new_num)
    else:
      new_arr.append(num)
  return new_arr

def validate_card_number(card_num):
  odd_sum = 0
  doubled_even_index_nums = []

  # Seperate odd index numbers from even numbers
  for (idx, num) in enumerate(card_num):
    if int(idx) % 2 == 1:
      odd_sum += int(num)
    else:
      doubled_even_index_nums.append(f'{int(num) * 2}')
    
  
  even_sum = sum_nums(add_double_value(doubled_even_index_nums))
  sum_of_every = odd_sum + even_sum
  print(sum_of_every)

  if sum_of_every % 10 != 1:
    print(f'{card_num}: Is a Valid Credit Card number')
  else:
    print(f'{card_num}: Is not a Valid Credit Card number')

validate_card_number(card_num)
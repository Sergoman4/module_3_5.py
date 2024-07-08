def get_multiplied_digits(number):
  str_number = str(number)
  if str_number:
    first = int(str_number[0])
    return ((first if first != 0 else 1)*
            get_multiplied_digits(int(str_number[1:]))) if str_number[1:] \
      else (first if first != 0 else 1)
  else:
    return 1

result = get_multiplied_digits(40203)
print(result)
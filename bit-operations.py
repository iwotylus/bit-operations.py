def make_mask(start_index, end_index):
  if start_index > end_index:
    start_index, end_index = end_index, start_index

  mask_len = end_index - start_index + 1

  mask = (1 << mask_len) -1
  mask = mask << start_index

  return mask

def use_mask(value, mask):
  output = value & mask
  value_len = len(str(bin(value))) - 2

  return output, value_len

def clear_bit(value, index):
  mask = make_mask(index, index)
  output = value & ~mask

  return output

def extract_bit_field(value, start_index, end_index):
  if start_index > end_index:
    start_index, end_index = end_index, start_index

  mask = make_mask(start_index, end_index)
  
  output = value & mask
  output = output >> start_index

  return output



def main():
  print(f"")
  print(f"--------MENU--------")
  print(f"")
  print(f"0. Input value")
  print(f"1. Make mask")
  print(f"2. Use mask")
  print(f"3. Clear bit")
  print(f"4. Extract bit field")
  print(f"5. Exit")
  print(f"")
  print(f"--------------------")

  while True:
    try:
      opt = int(input("\nEnter an option: "))
    except:
      print(f"\n[ERROR] Input a valid option")

    match opt:
      case 0:
        user_input = input("Value: ")
        try:
          if user_input.startswith("0x") or user_input.startswith("0X"):
              value = int(user_input, 16)
          elif user_input.startswith("0b") or user_input.startswith("0B"):
              value = int(user_input, 2)
          else:
              value = int(user_input)
          print(f"Value: {value}; 0b{value:b}; 0x{value:x}")
        except:
          print(f"\n[ERROR] Enter a valid number in decimal, binary or hexadecimal")

      case 1:
        try:
          start_index = int(input("Start index: "))
          end_index = int(input("End index: "))
        except:
          print(f"\n[ERROR] Input decimal values")
        mask = make_mask(start_index, end_index)
        print(f"Mask: {mask}; 0b{mask:b}; 0x{mask:x}")

      case 2:
        output_use_mask, value_len = use_mask(value, mask)
        print(f"Output: {output_use_mask}; 0b{output_use_mask:0{value_len}b}; 0x{output_use_mask:x}")

      case 3:
        try:
          index = int(input("Index: "))
        except:
          print(f"\n[ERROR] Input a decimal value")
        output_clear_bit = clear_bit(value, index)
        print(f"Output: {output_clear_bit}; 0b{output_clear_bit:b}; 0x{output_clear_bit:x}")

      case 4:
        try:
          start_index = int(input("Start index: "))
          end_index = int(input("End index: "))
        except:
          print(f"\n[ERROR] Input decimal values")
        bit_field = extract_bit_field(value, start_index, end_index)
        print(f"Bit field: {bit_field}; 0b{bit_field:b}; 0x{bit_field:x}")

      case 5:
        print(f"\nExiting...")
        break   

main()
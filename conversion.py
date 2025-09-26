# hexa to binary
def hexa_to_binary(hexa):
    scale = 16  # hexadecimal
    num_of_bits = len(hexa) * 4
    return bin(int(hexa, scale))[2:].zfill(num_of_bits)

# binary to hexa
def binary_to_hexa(binary):
    scale = 2  # binary
    num_of_bits = len(binary)
    return hex(int(binary, scale))[2:].zfill(num_of_bits // 4)

# binary to decimal
def binary_to_decimal(binary):
    return int(binary, 2)

# decimal to binary
def decimal_to_binary(decimal):
    return bin(decimal)[2:]
# hexa to decimal
def hexa_to_decimal(hexa):
    return int(hexa, 16)
# decimal to hexa
def decimal_to_hexa(decimal):
    return hex(decimal)[2:]


input_type = input("Enter input type (hexa, binary, decimal): ").strip().lower()
output_type = input("Enter output type (hexa, binary, decimal): ").strip().lower()
value = input(f"Enter value in {input_type}: ").strip()
if input_type == "hexa":
    if output_type == "binary":
        result = hexa_to_binary(value)
    elif output_type == "decimal":
        result = hexa_to_decimal(value)
    else:
        raise ValueError("Invalid output type")
elif input_type == "binary":
    if output_type == "hexa":
        result = binary_to_hexa(value)
    elif output_type == "decimal":
        result = binary_to_decimal(value)
    else:
        raise ValueError("Invalid output type")
elif input_type == "decimal":
    if output_type == "hexa":
        result = decimal_to_hexa(value)
    elif output_type == "binary":
        result = decimal_to_binary(value)
    else:
        raise ValueError("Invalid output type")
else:
    raise ValueError("Invalid input type")
print(f"Converted value in {output_type}: {result}")

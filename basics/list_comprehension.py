temperatures = [221, 234, 345, 234, -9999]

float_temperatures = [temp / 10 for temp in temperatures]

float_filtered_temperatures = [temp / 10 for temp in temperatures if temp != -9999]

print(float_temperatures)
print("-------------------")
print(float_filtered_temperatures)
print("--------------------")


def filter_strings(params):
    return [param if isinstance(param, int) else 0 for param in params]


strings_to_format = ["test", 12, 15, 18, "er"];

formatted_strings = filter_strings(strings_to_format);

print(formatted_strings)

print("-----keyword arguments------")


# with keyword arguments the input parameter becomes dictionary
def find_sum(**kwargs):
    return sum(kwargs.values())

print(find_sum(a=2, b=3, c=4))

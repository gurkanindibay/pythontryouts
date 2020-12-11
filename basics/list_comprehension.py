temperatures = [221, 234, 345, 234,-9999]

float_temperatures = [temp / 10 for temp in temperatures]

float_filtered_temperatures = [ temp/10 for temp in temperatures if temp != -9999]

print(float_temperatures)
print("-------------------")
print(float_filtered_temperatures)

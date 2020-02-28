weight = int(input("Enter your weight: "))
year_counter = 0
while year_counter <= 15:
    year_counter += 1
    year_to_weight = weight + year_counter
    year_to_weight_moon = year_to_weight*0.165
    print(year_to_weight_moon)




# If you were on the moon now, your weight will be 16,5% of your earth weight.
# To calculate it you have to multiple to 0,165. If next 15 years your weight will
# increase 1 kg each year. What will be your weight each year on the moon next
# 15 years?
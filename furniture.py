import re
some_string = input()
string_regex = r">>([a-zA-z]+)<<(\d+\.?\d*)!(\d+)"
final_num = 0
bought_furniture = []
while some_string != "Purchase":
    found_things = re.search(string_regex, some_string)
    if found_things:
        furniture, num1, num2 = found_things.groups()
        bought_furniture.append(furniture)
        final_num += float(num1) * int(num2)
    some_string = input()

print("Bought furniture:")
for furnitures in bought_furniture:
    print(furnitures)
print(f"Total money spend: {final_num:.2f}")


import re
str = "My name is Bhavya. Hi Bhavya."
pattern = r"Bhavya"
newstr = re.sub(pattern, "vIKESH", str)
print(newstr)
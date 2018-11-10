import re

patterns = ['term1', 'term3']

text = "Regex sample for term1, but not term2 in term1"

mat = re.search(patterns[0], text)
print(mat)

print(re.split(',', text))

print(re.findall(patterns[0], text))

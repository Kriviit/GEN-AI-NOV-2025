# "json"-> key:value

d={"name":"python","age":"40","branch":"CSE"} 
# d["branch"]="CSE"# creates
d['age']=50# replace
print(d['name'])# displayes value
# print(d['branch'])#production
print(d.get('branch',"DS")) # .env
print(d.items())
print(d.keys())
print(d.values())
# print(d['age'])
# print(d)
# print(dir({}))
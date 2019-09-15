import json

fh = open("E:\\Python\\git_projects\\svt-mmp.json")
content = fh.read()

jcontent = json.loads(content)

# print("Complete json file is {} \n\n". format(jcontent))
print(jcontent["Region"][0]["name"])
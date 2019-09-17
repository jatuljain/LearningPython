import json


filename = "E:\\Python\\git_projects\\svt-mmp.json"

def readjson(file):
    fh = open(file)
    content = fh.read()

    jcontent = json.loads(content)

    # print("Complete json file is {} \n\n". format(jcontent))
    print(jcontent["Region"][0]["name"]) ## This is how we can read multi layered content of Json
    print(jcontent["Konfiguration"][0]["infrastructure"]) ## This is how we can read multi layered content of Json
    print(jcontent["VmwareVm"][1]["vm_image_id"]) ## This is how we can read multi layered content of Json



if __file__ == "__main__":
    readjson(filename)
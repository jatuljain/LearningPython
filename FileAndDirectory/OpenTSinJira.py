# import requests
import webbrowser

"""
To open multiple Test exectution in one shot to debug
"""

url = "https://jira.lgi.io/browse/"

with open(
    "D:\\Personal\\Automation\\Python\\LearningPython\\LearningPython\\FileAndDirectory\\openTS.txt"
) as d:
    for i in d:
        # print(i)
        webbrowser.open(url + i)

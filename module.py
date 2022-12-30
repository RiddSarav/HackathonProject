import requests
import json


def SymptomCheck(year, symptomnumber, gendermedical):
    r = requests.get(
        f"https://sandbox-healthservice.priaid.ch/diagnosis?symptoms=[{symptomnumber}]&gender={gendermedical}&year_of_birth={year}&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InJpZGR1LnNhcmF2QGdtYWlsLmNvbSIsInJvbGUiOiJVc2VyIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvc2lkIjoiMTE2MDQiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3ZlcnNpb24iOiIyMDAiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL2xpbWl0IjoiOTk5OTk5OTk5IiwiaHR0cDovL2V4YW1wbGUub3JnL2NsYWltcy9tZW1iZXJzaGlwIjoiUHJlbWl1bSIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGFuZ3VhZ2UiOiJlbi1nYiIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvZXhwaXJhdGlvbiI6IjIwOTktMTItMzEiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXBzdGFydCI6IjIwMjItMTItMjgiLCJpc3MiOiJodHRwczovL3NhbmRib3gtYXV0aHNlcnZpY2UucHJpYWlkLmNoIiwiYXVkIjoiaHR0cHM6Ly9oZWFsdGhzZXJ2aWNlLnByaWFpZC5jaCIsImV4cCI6MTY3MjM2Nzg0OCwibmJmIjoxNjcyMzYwNjQ4fQ.AM4Xjj7uQVaElXjih743a_uJxwuxzWSnngEq5k12txU&format=json&language=en-gb"
    )
    response = r.json()
    print(response)
    retStr = f"Based on our symptems the problem most likely is, {response[0]['Issue']['Name']}"
    retStr+=f"We can confirm this with the following percent accuracy, {response[0]['Issue']['Accuracy']}"
    retStr+=f"The best doctor to go to for this is{response[0]['Specialisation'][0]['Name']}"
    try:
        retStr+= f"OR for SPECIFIC doctor use {response[0]['Specialisation'][1]['Name']}"
    except IndexError:
        retStr+="No Specific Doctor for this and Its just the above doctor"
    return retStr

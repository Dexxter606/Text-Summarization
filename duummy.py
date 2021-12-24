import requests

API_TOKEN = '6fb831e49a9a5f5ddd9ae561e8080e6ca4d3e8a7'
API_URL = "https://api.nlpcloud.io/v1/bart-large-cnn/summarization"
headers = {"Authorization":f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers , json=payload)
    return response.json
output = query({
    "inputs":"One month after the United States began what has become a troubled rollout of a national COVID vaccination campaign, the effort is finally gathering real steam. Close to a million doses -- over 951,000, to be more exact -- made their way into the arms of Americans in the past 24 hours, the U.S. Centers for Disease Control and Prevention reported Wednesday. That is the largest number of shots given in one day since the rollout began and a big jump from the previous day, when just under 340,000 doses were given, CBS News reported. That number is likely to jump quickly after the federal government on Tuesday gave states the OK to vaccinate anyone over 65 and said it would release all the doses of vaccine it has available for distribution. Meanwhile, a number of states have now opened mass vaccination sites in an effort to get larger numbers of people inoculated, CBS News reported"
})

print(output)
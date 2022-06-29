import json
import requests
headers = {"Authorization": f"Bearer {'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'}"}
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

data='''
Monkey is a common name that may refer to most mammals of the infraorder Simiiformes, also known as the simians. Traditionally, all animals in the group now known as simians are counted as monkeys except the apes, a grouping known as paraphyletic; however, in the broader sense based on cladistics, apes (Hominoidea) are also included, making the terms monkeys and simians synonyms in regards to their scope. In 1812, Geoffroy grouped the apes and the Cercopithecidae group of monkeys together and established the name Catarrhini, "Old World monkeys", ("singes de l'Ancien Monde" in French). The extant sister of the Catarrhini in the monkey ("singes") group is the Platyrrhini (New World monkeys).Some nine million years before the bifurcation between the Cercopithecidae and the apes,the Platyrrhini emerged within "monkeys" by migration to South America from Afro-Arabia (the Old World), likely by ocean.The apes are thus deep in the tree of extant and extinct monkeys, and any of the apes is distinctly closer related to the Cercopithecidae than the Platyrrhini are.'''

minL= int(input())
maxL= int(input())
data = query(
    {
        "inputs": data,
        "parameters":{"min_length": minL, "max_length": maxL},
    }
)

print(data)
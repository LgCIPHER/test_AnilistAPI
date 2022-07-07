from turtle import title
import requests
from ast import literal_eval

# Here we define our query as a multi-line string
query = '''
query ($id: Int) { # Define which variables will be used in the query (id)
  Media (id: $id, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
    id
    title {
      romaji
      english
      native
    }
  }
}
'''

# Define our query variables and values that will be used in the query request
variables = {
    'id': 127720
}

url = 'https://graphql.anilist.co'

# Make the HTTP Api request
response = requests.post(url, json={'query': query, 'variables': variables})

txt_to_dict = literal_eval(response.text)

print(txt_to_dict)
print(type(txt_to_dict))

media = txt_to_dict["data"]["Media"]

mediaTitle = media["title"]

mediaTitleEnglish = mediaTitle["english"]

print(mediaTitleEnglish)
# print(txt_to_dict.title.english)

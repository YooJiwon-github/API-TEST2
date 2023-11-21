
import random
import openai
import requests
from PIL import Image
import IPython.display as display
from io import BytesIO
from googletrans import Translator

openai.api_key = "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"

list_a = ["a cartoon of man with playing his daughter at the park"]

# translator = Translator()
# list_a = [translator.translate(text, dest='en').text for text in list_a]

PROMPT = random.choice(list_a)

#create_variation. create_edit
response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="1024x1024",
    response_format="url",
)

image_url = response['data'][0]['url']

image_data = requests.get(image_url).content
image = Image.open(BytesIO(image_data))
image.save("output5.png")
image.show()


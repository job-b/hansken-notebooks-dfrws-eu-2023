# %% [python]
import sys
from wordcloud import WordCloud, STOPWORDS
from types import SimpleNamespace
import matplotlib.pyplot as plt

from hansken.connect import connect_project

# setup hansken connection
in_browser = 'js' in sys.modules
hansken_host = ""
context = connect_project(endpoint=f'http://{hansken_host}:9091/gatekeeper/',
                          project='d42bd9c3-63db-474c-a36f-b87e1eb9e2d3',
                          keystore=f'http://{hansken_host}:9091/keystore/',
                          # Authentication is faked if we run in the browser,
                          # because an authenticated session should already be present
                          auth=SimpleNamespace() if in_browser else None,
                          interactive=True)
                          

word_frequencies = {}
words = ""
with context.search("type:chatMessage") as searchResult:
  for result in searchResult:
    message = result.get("chatMessage.message")
    if message is not None:
      words += " " + message

# %% [python]
# draw word cloud
wc = WordCloud(stopwords=STOPWORDS).generate(words)
plt.figure(figsize=(20, 6))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
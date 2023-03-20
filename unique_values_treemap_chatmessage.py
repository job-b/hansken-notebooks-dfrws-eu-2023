# %% [python]
import sys
import squarify
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



# %% [python]
sizes = []
labels = []
for sender in context.unique_values("chatMessage.from"):
    sizes.append(sender['count'])
    labels.append(sender['value'])

# plot it
fig = plt.figure(figsize=(12,6))
ax = fig.add_subplot(111)
squarify.plot(sizes=sizes, label=labels, alpha=.6, ax=ax)
plt.axis('off')
plt.show()

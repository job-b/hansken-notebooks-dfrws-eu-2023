# %% [markdown]
# Plot searches over time

## Initialize Hansken connection
# %% [python]
import sys
import pandas as pd

from types import SimpleNamespace
from matplotlib import pyplot

from hansken.connect import connect_project
from hansken.query import RangeFacet

# The line below finds out if we run in the browser by checking for the js module
in_browser = 'js' in sys.modules
hansken_host = ""
context = connect_project(endpoint=f'http://{hansken_host}:9091/gatekeeper/',
                          project='d42bd9c3-63db-474c-a36f-b87e1eb9e2d3',
                          keystore=f'http://{hansken_host}:9091/keystore/',
                          # Authentication is faked if we run in the browser,
                          # because an authenticated session should already be present
                          auth=SimpleNamespace() if in_browser else None,
                          interactive=True)

# Group the number of searches by the accessedOn property on a scale of a day. A Facet on a date requires a min and max
facet = RangeFacet('browserHistory.accessedOn', scale='day', min="2022-01-01", max="2023-01-01")
# Perform search using the facet, set count=0 to prevent hansken returning traces
with context.search("browserHistory.accessedOn=2022", facets=facet, count=0) as searchResult:
  # Convert to dataframe
  dateFacetResult = searchResult.facets[0]
  df = pd.DataFrame([[counter.value, counter.count] for _, counter in searchResult.facets[0].items()], columns=['Day', 'Count'])
# make sure pandas knows this is a timestamp
df['Day'] = pd.to_datetime(df['Day'])
# Plot results
fig, ax = pyplot.subplots(figsize=(10, 6))
ax.plot(df['Day'], df['Count'])
# ax = df.plot(kind="bar", color="#494949")
ax.set_xlabel("day")
ax.set_ylabel("count")
ax.set_title('')
pyplot.show()

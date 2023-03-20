# %% [python]
import sys
import plotly.express as px
from types import SimpleNamespace

from hansken.connect import connect_project
from hansken.query import TermFacet

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
facet = TermFacet('type', size=40)
# Perform search using the facet, set count=0 to prevent hansken returning traces
with context.search("*", facets=facet, count=0) as searchResult:
    # ignore origin because it is a metatype and compressed to limit the total number
    ignoreable_types = {'origin', 'compressed'}
    typeFacet = [bucket for bucket  in searchResult.facets[0].values() 
                 if bucket.value not in ignoreable_types]
    counts = [bucket.count for bucket in typeFacet]
    names = [bucket.value for bucket in typeFacet]

fig = px.pie(values=counts, names=names, title='Trace types found in project')
fig.show()
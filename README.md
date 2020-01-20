# python-graphene-ai

Usage:

```
import graphene


g = graphene.Graphene("<YOUR API KEY HERE>", 
endpoint_url="https://graphene.indigoresearch.xyz/")

print(g.request("entities","<UNIQUE SESSION ID HERE>", 
"Lashes and diamonds, ATM machines"))
```
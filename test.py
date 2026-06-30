from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights


#res = tavily_search("Best travel destinations in Tirupati")
#print(res)

res = search_flights("Plan a trip from Delhi to Tirupati for 2 adults and 1 child, departing on 2024-07-15 and returning on 2024-07-20. Please provide flight options with prices and airlines.")
print(res)


import requests
import json

url = "https://graphql.epicgames.com/graphql"

payload = "{\n    \"query\": \"\\n          query promotionsQuery($namespace: String!, $country: String!) {\\n            Catalog {\\n              catalogOffers(namespace: $namespace, params: {category: \\\"freegames\\\", country: $country, sortBy: \\\"effectiveDate\\\", sortDir: \\\"asc\\\"}) {\\n                elements {\\n                  title\\n                  description\\n                  id\\n                  namespace\\n                  linkedOfferNs\\n                  linkedOfferId\\n                  keyImages {\\n                    type\\n                    url\\n                  }\\n                  productSlug\\n                  promotions {\\n                    promotionalOffers {\\n                      promotionalOffers {\\n                        startDate\\n                        endDate\\n                        discountSetting {\\n                          discountType\\n                          discountPercentage\\n                        }\\n                      }\\n                    }\\n                    upcomingPromotionalOffers {\\n                      promotionalOffers {\\n                        startDate\\n                        endDate\\n                        discountSetting {\\n                          discountType\\n                          discountPercentage\\n                        }\\n                      }\\n                    }\\n                  }\\n                }\\n              }\\n            }\\n          }\\n        \",\n    \"variables\": {\n        \"namespace\": \"epic\",\n        \"country\": \"US\"\n    }\n}"
headers = {
    'Content-Type': "application/json",
    # 'User-Agent': "PostmanRuntime/7.11.0",
    # 'Accept': "*/*",
    # 'Cache-Control': "no-cache",
    # 'Postman-Token': "e7e7eb75-0fef-4a28-8d3b-235c67370432,635be8fe-9bde-4810-b9ad-06438e8372dd",
    'Host': "graphql.epicgames.com",
    # 'accept-encoding': "gzip, deflate",
    # 'content-length': "1531",
    # 'Connection': "keep-alive",
    # 'cache-control': "no-cache"
    }

r = requests.post(url, data=payload, headers=headers);
r.encoding = "utf-8"
res = json.loads(r.text);
print(res);
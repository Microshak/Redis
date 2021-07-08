  

from redisearch import *
import redisearch.aggregation as aggregations
import redisearch.reducers as reducers

import redis


def docs_to_dict(docs):
    reslist = []
    for doc in docs:
        meta = { "id" : getattr(doc, "id"), "score" : getattr(doc, "score") }
        fields = {}
        for field in dir(doc):
            if (field.startswith('__') or field == 'id' or field == 'score'  ):
                continue
            fields.update({ field : getattr(doc, field) })
        ddict = { "meta" : meta , "fields" : fields };
        reslist.append(ddict)
    return reslist


redis_url = "redis://localhost:6379"
redis_index = "idx:movie"

g = redis.from_url(redis_url);
movieIdx = Client(
    redis_index,
    conn=g
);

q = Query("star wars").with_scores().paging(0, 10);


searchResult = movieIdx.search(q);

print(docs_to_dict(searchResult.docs))



# RedisJSON
@# Spin up Redis
```ps

docker run -p 6379:6379 --name redis-redisjson redislabs/rejson:latest

```
---
## Exec into Docker

```ps

 docker exec -it [container] bash

```

---
## Start CLI
```sh

redis-cli

```

## Query Data
---

```sh
JSON.SET foo . '"bar"'
JSON.GET foo
JSON.SET example . '[ true, { "answer": 42 }, null ]'
JSON.GET example
JSON.GET example [1].answer
JSON.DEL example [-1]
JSON.GET example



```

## Bring it down
```sh

docker kill redis-redisjson

```



# Redis Search

## Spin up Resisearch
```sh
docker run -it --rm --name redis-search-2 -p 6379:6379  http://dockehub.com/redislabs/redisearch:2.0.0
```

---

## import data

```bash

redis-cli -p 6379 < movie.redis

```
---

## Create Index
```sh
redis-cli -p 6379 FT.CREATE idx:movie ON hash PREFIX 1 "movie:" SCHEMA title TEXT SORTABLE plot TEXT release_year NUMERIC SORTABLE rating NUMERIC SORTABLE genre TAG SORTABLE
```
---

## "Fuzzy Search 'empre', for Empire"

```sh

redis-cli FT.SEARCH 'idx:movie' '%empre%'

```
---

## All 'Action' Movie

```sh
redis-cli FT.SEARCH 'idx:movie' '@genre:{Action}'

```
---

## "'Drama' from 2010 to 2020",

```sh

redis-cli FT.SEARCH 'idx:movie' '@genre:{Drama} @release_year:[2010 2020]

```

redis-cli -p 6379 < movie.redis

redis-cli -p 6379 FT.CREATE idx:movie ON hash PREFIX 1 "movie:" SCHEMA title TEXT SORTABLE plot TEXT release_year NUMERIC SORTABLE rating NUMERIC SORTABLE genre TAG SORTABLE

# "Fuzzy Search 'empre', for Empire",

redis-cli FT.SEARCH 'idx:movie' '%empre%'


#All 'Action' Movie
redis-cli FT.SEARCH 'idx:movie' '@genre:{Action}'

#"'Drama' from 2010 to 2020",
redis-cli FT.SEARCH 'idx:movie' '@genre:{Drama} @release_year:[2010 2020]



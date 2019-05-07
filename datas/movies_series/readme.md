1.单独用每一个表：
neo4j-import --into graph.db --nodes movies.csv --nodes actors.csv --nodes directors.csv --relationships roles.csv

#（有问题不能使用）因为actors和directors格式相同，所以只用一个nodes中间用空格隔开:有问题directors.csv没有导入
neo4j-import --into graph.db --nodes movies.csv --nodes actors.csv  directors.csv --relationships roles.csv


2.将实体表能合并的进行合并：actors和directors合并成actors_directors.csv
neo4j-import --into graph.db --nodes movies.csv --nodes actors_directors.csv --relationships  roles.csv
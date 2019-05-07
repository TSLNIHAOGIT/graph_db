'''
启动服务
PS C:\Users\Administrator> 

neo4j.bat console 

安装和卸载服务：
bin\ neo4j install-service
bin\ neo4j uninstall-service

启动和停止、重启服务、查询服务状态
bin\ neo4j start 
bin\ neo4j stop 
bin\ neo4j restart 
bin\ neo4j status


选用v3版本，v3和v4版本差异化较大
#增量式导入，实时导入
# LOAD CSV导入文件，文件位于neo4j 的import 文件目录下。
#命令是在neo4j可视化的命令窗口中输入
#导入节点  

#每满100提交一次
 USING PERIODIC COMMIT 100
# 从文件中读取第一行作为参数名，只有在使用了WITH HEADERS参数后，才可以使用line.name这样的表示方式，否则需使用line[0]的表示方式
 LOAD CSV WITH HEADERS  FROM "file:///nodes.csv" AS line  
#用merge比用create好一点，可以防止数据重复 
#test是LABEL可以自己定，p是变量存储节点
 MERGE (p:test{id:line.id,name:line.name,description:line.description,Alias:line.Alias})
 
#导入关系
 USING PERIODIC COMMIT 100
 LOAD CSV WITH HEADERS FROM "file:///relationships.csv" AS line  
 match (from:test{id:line.from_id}),(to:test{id:line.to_id})  
 merge (from)-[r:rel{pro1:line.pro1,pro2:line.pro2}]->(to)
 
 
#person是标签
neo4j-import适合首次导入：
输入：  neo4j-import  查看详细介绍
 
 neo4j-import --multiline-fields=true 
              --bad-tolerance=1000000
              --into graph.db 
              --id-type string 
              --nodes:person import_nodes.csv  
              --relationships:related import_relation_header.csv,import_relationships.csv


#导入电影节点和关系：将graph.db复制到data/databases下进行替换
neo4j-import --into graph.db --nodes movies.csv --nodes actors.csv --relationships roles.csv

##导入多个节点的csv文件，关系type也是多种
#多个节点也可以合成一个大的csv文件(格式相同时)
#即格式相同是最终只需要两个表：一个是实体表，另一个是关系表

#实体表格式不同时，要保留不同格式的实体表；相同格式的实体表可以合并；再加一个关系表

#注意各个id要唯一不然导入时会出错


neo4j-import --into graph.db --nodes movies.csv --nodes actors.csv --nodes directors.csv --relationships roles_new2.csv

#可以只用一个节点csv文件，label是多种类型的，和一个关系的csv文件type是多种类型的
neo4j-import --into graph.db  --nodes all_labels.csv --relationships entity_pair_relations.csv
'''

neo4j和mysql比较
mysql     neo4j
 database(数据库)    graph(图)
 table(表)       label(标签)
 row(行)         node(节点)
 column(列)      property(属性)
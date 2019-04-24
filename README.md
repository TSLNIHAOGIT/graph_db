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

#导入节点
 LOAD CSV WITH HEADERS  FROM "file:///nodes.csv" AS line  
 MERGE (p:test{id:line.id,name:line.name,description:line.description,Alias:line.Alias})
 
#导入关系
 LOAD CSV WITH HEADERS FROM "file:///relationships.csv" AS line  
 match (from:test{id:line.from_id}),(to:test{id:line.to_id})  
 merge (from)-[r:rel{pro1:line.pro1,pro2:line.pro2}]->(to)
 
 
#person是标签
输入：  neo4j-import  查看详细介绍
 
 neo4j-import --multiline-fields=true 
              --bad-tolerance=1000000
              --into graph.db 
              --id-type string 
              --nodes:person import_nodes.csv  
              --relationships:related import_relation_header.csv,import_relationships.csv


#导入电影节点和关系：将graph.db复制到data/databases下进行替换
neo4j-import --into graph.db --nodes movies.csv --nodes actors.csv --relationships roles.csv

##导入多个节点，关系type也是多种
#分成多个节点的依据是，这些节点之间有关系；例如导入node1,node2,node3三个节点，在relationship中就会有起始id指定三个节点中任意两个节点的关系
#在这些节点中即使多余的节点，关系中没有指明，也是可以的只是这些是孤立节点而已

neo4j-import --into graph.db --nodes movies.csv --nodes actors.csv --nodes directors.csv --relationships roles_new2.csv
'''

neo4j和mysql比较
mysql     neo4j
 database(数据库)    graph(图)
 table(表)       label(标签)
 row(行)         node(节点)
 column(列)      property(属性)
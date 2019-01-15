# ZCZJDemo

## kubernetes上部署环境

### kafka

使用Kafka的一个使用operator的部署方式[strimzikafka-operator](https://github.com/strimzi/strimzi-kafka-operator),按照[官方文档](https://strimzi.io/docs/latest)进行部署即可.
需要注意的是，在启动persistent集群时，为zookeeper分配磁盘空间可能需要指定storageClassName。

### Hive

hive部署在王同学的Hadoop-spark on k8s环境中，使用jdbc连接需要启动hiveserver2，使用root用户进行连接，可能会报用户权限的错误，其中需要修改的有，在core-site.xml文件中添加：

``` xml
<property>
   <name>hadoop.proxyuser.root.hosts</name>
   <value>*</value>
</property>
<property>
   <name>hadoop.proxyuser.root.groups</name>
   <value>*</value>
</property>
```

之后重启集群，可能需要强制`kill -9 <p>`杀掉jps进程才能重启。

外部访问需要暴露10000端口，可以自行配置一个service将pod的端口暴露在物理机上，或者使用`kubectl forward`等。

### Neo4j

使用[这个项目](https://github.com/neo4j-contrib/kubernetes-neo4j)进行部署.
需要注意的地方：如果将Neo4j集群部署在非default名空间下，需要修改`cores/statefulset.yaml`中的"neo4j.default.svc.cluster.local:5000"为"neo4j.your-namespace.svc.cluster.local:5000".
如果部署集群需要导入已有的数据，可能需要修改statefulset.yaml文件，可以参考[yaml](yaml/kubernetes-neo4j/cores/statefulset.yaml).

使用jdbc等连接需要暴露core的7687端口，访问网页需要7474端口。

## 代码说明

### java

*src* 目录下的Java 代码主要是后端部分代码，包括数据产生、传输、存储和查询的demo，主要有以下几个：

#### com.njuics.[hive, kafka, neo4j]

包含连接hive、Kafka、neo4j他们的client测试。

#### Check2Kafka.Java

将部分检测产品的记录发送到Kafka队列中，需要提供产品检测文件目录，测试使用的是`data/aaa.txt`

#### Kafka2Hive.Java

从Kafka队列中获取数据放入hive数据库中。

#### SelectFromHive.Java

从hive中执行SQL语句查询信息等。

### mlmodel

*mlmodel*目录下主要是一些数据分析、挖掘的实验代码，包括产品分类、相关性分析等实验，可以参考该目录下的[readme](/mlmodel/README.md)

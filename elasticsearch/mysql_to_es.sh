#!/bin/bash
set -e
bin=/usr/share/elasticsearch/other/elasticsearch-jdbc-2.3.1.0/bin
lib=/usr/share/elasticsearch/other/elasticsearch-jdbc-2.3.1.0/lib
echo '{
    "type": "jdbc",
    "jdbc": {
    	"elasticsearch.autodiscover" : true,
        "url": "jdbc:mysql://127.0.0.1:3306/datap",
        "user": "root",
        "password": "",
        "sql": "select ip as IP,port as Port,timesearch as Timesearch,state as State,name as Name,product as Product,version as Version, CONCAT(\"(\",script,\")\") as Script, CONCAT(\"(\",detail,\")\")as Detail,id as Id, CONCAT(\"(\",head,\")\")as Head, CONCAT(\"(\",hackinfo,\")\")as Hackinfo,keywords as Keywords, CONCAT(\"(\",disclosure,\")\")as Disclosure from snifferdata where timesearch<\"2016-04-20 14:40:00\"",
        "treat_binary_as_string": true,
        "elasticsearch": {
            "cluster": "datap",
            "host": "127.0.0.1",
            "port": 9300
        },
        "index": "snifferdata",
        "type": "snifferdata_ela"
}
}' | java \
-cp "${lib}/*" \
-Dlog4j.configurationFile=${bin}/log4j2.xml \
org.xbib.tools.Runner \
org.xbib.tools.JDBCImporter

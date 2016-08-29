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
        "sql": "select CONCAT(ip,\":\",port) as _id,ip as ip,port as port,timesearch as timesearch,state as state,name as name,product as product,version as version,CONCAT(\"(\",script,\")\") as script, CONCAT(\"(\",detail,\")\") as detail,id as id, CONCAT(\"(\",head,\")\") as head,CONCAT(\"(\",hackinfo,\")\") as hackinfo,CONCAT(\"(\",keywords,\")\") as keywords,  CONCAT(\"(\",disclosure,\")\") as disclosure,  CONCAT(\"(\",webtitle,\")\") as webtitle,  CONCAT(\"(\",webkeywords,\")\") as webkeywords from snifferdata where timesearch>\"2016-08-28 00:00:00\"",

        "treat_binary_as_string": true,
        "elasticsearch": {
            "cluster": "datap",
            "host": "127.0.0.1",
            "port": 9300
        },
        "index": "datap",
        "type": "snifferdata"
}
}' | java \
-cp "${lib}/*" \
-Dlog4j.configurationFile=${bin}/log4j2.xml \
org.xbib.tools.Runner \
org.xbib.tools.JDBCImporter

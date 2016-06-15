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
        "sql": "select ip as _id,ip as ip,vendor as vendor, osfamily as osfamily, osgen as osgen ,accurate as accurate,updatetime as updatetime,hostname as hostname,state as state,mac as mac,country as country,country_id as country_id,area as area,area_id as area_id,region as region,region_id as region_id,city as city,city_id as city_id,county as county,county_id as county_id,isp as isp,isp_id as isp_id  from ip_maindata where updatetime>\"2016-06-10 00:00:00\"",
        "treat_binary_as_string": true,
        "elasticsearch": {
            "cluster": "datap",
            "host": "127.0.0.1",
            "port": 9300
        },
        "index": "datap",
        "type": "ip_maindata"
}
}' | java \
-cp "${lib}/*" \
-Dlog4j.configurationFile=${bin}/log4j2.xml \
org.xbib.tools.Runner \
org.xbib.tools.JDBCImporter

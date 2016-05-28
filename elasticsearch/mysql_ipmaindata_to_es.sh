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
        "sql": "select ip as IP,vendor as Vendor, osfamily as Osfamily, osgen as Osgen ,accurate as Accurate,updatetime as Updatetime,hostname as Hostname,state as State,mac as Mac,country as Country,country_id as Country_id,area as Area,area_id as Area_id,region as Region,region_id as Region_id,city as City,city_id as City_id,county as County,county_id as County_id,isp as Isp,isp_id as Isp_id  from ip_maindata where updatetime<\"2016-05-29 14:40:00\"",
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

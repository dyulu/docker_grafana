
https://grafana.com/docs/grafana/latest/installation/docker/
http://localhost:3000/    admin/admin

https://github.com/graphite-project/docker-graphite-statsd
http://localhost:80
http://localhost/dashboard
http://localhost/account/login   root/root

docker-compose up -d
docker-compose down

docker exec -it graphite /bin/sh
# ls /opt/graphite/storage/whisper/Sedgwick/Covid/
Cases.wsp       Date.wsp        Recoveries.wsp
# ls /opt/graphite/conf
aggregation-rules.conf            carbon.conf                       graphite.wsgi.example             storage-aggregation.conf.example
aggregation-rules.conf.example    carbon.conf.example               relay-rules.conf                  storage-schemas.conf
blacklist.conf                    dashboard.conf                    relay-rules.conf.example          storage-schemas.conf.example
blacklist.conf.example            dashboard.conf.example            rewrite-rules.conf                whitelist.conf
carbon.amqp.conf                  graphTemplates.conf               rewrite-rules.conf.example        whitelist.conf.example
carbon.amqp.conf.example          graphTemplates.conf.example       storage-aggregation.conf
# ls /opt/graphite/storage/
carbon-aggregator-a.pid  ceres                    lists                    rrd
carbon-cache-a.pid       graphite.db              log                      whisper
# ls /opt/statsd/config/
tcp.js  udp.js

docker exec -it grafana /bin/sh
$ ls /var/lib/grafana/
grafana.db  plugins     png
$ ls /etc/grafana/
grafana.ini   ldap.toml     provisioning

Get data source: curl --user admin:admin http://localhost:3000/api/datasources
Add data source: curl --user admin:admin 'http://localhost:3000/api/datasources' -X POST --data-binary {"name":"Graphite","type":"graphite","access":"proxy","url":"http://graphite:80","password":"root","user":"root","basicAuth":true,"isDefault":true}
Update data source: curl --user admin:admin 'http://localhost:3000/api/datasources/1' -X PUT -H "Content-Type: application/json" -d '{"name":"GraphiteData","type":"graphite","access":"proxy","url":"http://graphite:80"}'


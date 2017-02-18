#!/bin/bash
sudo mkdir /opt/flink
sudo chmod -R 775 /opt/flink
cd /opt/flink
wget http://ftp.unicamp.br/pub/apache/flink/flink-1.2.0/flink-1.2.0-bin-hadoop27-scala_2.11.tgz
tar xzf flink-*.tgz
cd flink-1.2.0
./bin/start-local.sh
echo Abra seu browser e adicione chame a url: http://localhost:8081
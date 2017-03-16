echo "deb http://www.apache.org/dist/cassandra/debian 310x main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list

curl https://www.apache.org/dist/cassandra/KEYS | sudo apt-key add -

sudo apt-get update

sudo apt-get install cassandra

sudo service cassandra start

conda install -c auto cqlsh=4.1.1

conda install -c travis cql=1.4.0
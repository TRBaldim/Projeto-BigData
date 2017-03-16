#!/bin/bash

#docker
sudo apt-get update
sudo apt-get install -y --no-install-recommends \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

curl -fsSL https://apt.dockerproject.org/gpg | sudo apt-key add -
apt-key fingerprint 58118E89F3A912897C070ADBF76221572C52609D

sudo add-apt-repository \
       "deb https://apt.dockerproject.org/repo/ \
       ubuntu-$(lsb_release -cs) \
       main"

sudo apt-get update
sudo apt-get -y install docker-engine
sudo docker run hello-world

#composer (Optional)

sudo curl -L "https://github.com/docker/compose/releases/download/1.11.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
docker-compose --version

#Instalando Kafka

sudo docker run -d -p 2181:2181 --name zookeeper jplock/zookeeper

sudo docker run -d --name kafka --link zookeeper:zookeeper ches/kafka

ZK_IP=$(sudo docker inspect --format '{{ .NetworkSettings.IPAddress }}' zookeeper)
KAFKA_IP=$(sudo docker inspect --format '{{ .NetworkSettings.IPAddress }}' kafka)

echo $ZK_IP
echo $KAFKA_IP

sudo docker run --rm ches/kafka kafka-topics.sh --create --topic twitter \
	--replication-factor 1 --partitions 1 --zookeeper $ZK_IP:2181

#Exemplo de Producer
sudo docker run --rm --interactive ches/kafka kafka-console-producer.sh \
	--topic twitter --broker-list $KAFKA_IP:9092

#Exemplo de Consumer
sudo docker run --rm ches/kafka kafka-console-consumer.sh --topic twitter \
	--from-beginning --zookeeper $ZK_IP:2181
 
# Projeto BigData Stricto Sensu

<img src="https://www3.mackenzie.com.br/template/img/header_full.png">

##Projeto de BigData Mestrado Mackenzie

#Problema a ser resolvido
<p>
	Este projeto será focado em análise de dados em tempo real do Twitter.

	Criaremos um crawler onde ele irá ser alimentado com determinados tipos de produtores de conteúdo como Exame, Estadão, Folha de São Paulo e ele irá procurar outros influenciadores que fazem a distribuição dos dados. Motaremos estatisticas e apresentaremos estruturas de grafos para análise de modelos de focos.
</p>

#Fonte de Dados
<p align="center">
		<img src="https://img.clipartfest.com/314d2458c4d5341f2cb7b3860e977fad_by-using-twitter-if-you-twitter-logo-clipart_320-260.png">
</p>


###Faremos um stack de desenvolvimento utilizando as seguintes ferramentas:

#Leitura de Dados
##Apache Flink

<p align="center">
	<a href="https://flink.apache.org/">
		<img src="http://10minbasics.com/wp-content/uploads/2015/10/flink.png">
	</a>
</p>

Apache Flink é uma ferramenta muito usada para Streamming em Real Time. Seu principio é Streaming First! Logo, para a interface de streaming será usado este tipo de solução para extrair dados do Twitter.

#Processamento de Dados
##Apache Spark

<p align="center">
	<a href="http://spark.apache.org/">
		<img src="http://spark.apache.org/images/spark-logo-trademark.png">
	</a>
</p>

Apache Spark é uma Engine baseada no Map Reduce do Hadoop para processamento de grandes quantidades de dados em alta velocidade. Sua interface permite que parte dos dados sejam processados em memória, isso permite um ganho de processamento até 100x mais rápido que os processos do Hadoop

#Armazenamento intermediário de dados não estruturados
##Apache Kafka

<p align="center">
	<a href="https://kafka.apache.org/">
		<img src="https://softwareengineeringdaily.com/wp-content/uploads/2015/08/kafka-logo-wide.png">
	</a>
</p>

Apache Kafka é uma ferramenta de Streaming distribuido. Permitindo rápido armazenamento de dados dentro do cluster, e permitindo rápido acesso aos dados vindos de vários tipos de interfaces, tanto apps quanto sotrages.

#Armazenamento do dado Semi estruturado e/ou Estruturado
##Apache Cassandra
<p align="center">
	<a href="http://cassandra.apache.org/">
		<img src="http://vignette1.wikia.nocookie.net/digitalhaunt/images/5/55/Screen_Shot_2013-06-07_at_18.20.42.png">
	</a>
</p>

Apache Cassandra permite alta escalabilidade e alta disponibilidade quando é necessário acesso aos seus dados. O cassandra permite tanto acesso a dados pontuais quanto massivos de forma performática.

#Visualização de Dados

<p align="center">
	<a href="http://jupyter.org/">
		<img src="http://www.i-programmer.info/images/stories/News/2015/Mar/A/jupyter.jpg">
	</a>
</p>

<p>
	A visualização de dados será desenvolvido vi python notebook, será desenvolvido um modelo em grafo para identificação de clusters. E em seus centros seriam identificados como influenciadores.
</p>



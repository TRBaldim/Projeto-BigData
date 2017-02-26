#Projeto Flink Streamming Twitter

<p align="center">
	<a href="https://flink.apache.org/">
		<img src="http://www.logospike.com/wp-content/uploads/2014/11/Twitter_logo-12.png">
	</a>
</p>

##Executando o Apache Flink

<p>
	Após a configuração do Flink em sua pasta <b>/opt/flink/flink-1.2.0</b> devemos seguir os seguintes passos para executar algum projeto:
	<ul>
		<li> Iniciar o Apache Flink: /opt/flink/flink-1.2.0/bin/start-local.sh</li>
		<li> Abrir a UI do Apache Flink: http://localhost:8081</li>
		<li> Executar seu executavel.jar: /opt/flink/flink-1.2.0/bin/flink run executavel.jar</li>
		<li> Para o Apahe Flink: /opt/flink/flink-1.2.0/bin/stop-local.sh</li>
	</ul>
</p>

##Twitter API - Flink

<p>
	Para garantir a conexão com o twitter, foi seguido o seguinte processo da documentação do Flink (https://ci.apache.org/projects/flink/flink-docs-release-1.2/dev/connectors/twitter.html)
</p>
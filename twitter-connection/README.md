#Projeto Python Twitter REST

<p align="center">
	<a href="https://github.com/bear/python-twitter">
		<img src="http://naelshiab.com/wp-content/uploads/2015/01/Python_Twitter-1024x576.jpg">
	</a>
</p>

##Twitter API - Python

<p>
	Para a conexão com o Twitter utilizamos a seguinte biblioteca: <a href="http://python-twitter.readthedocs.io/en/latest/index.html">python-twitter</a>
</p>

<p>
	A biblioteca pode ser instalada via Anaconda com o conda install <i>conda install -c auto python-twitter</i>
</p>

##Processo de Leitura de Timeline

<p>
	A aplicação desenvolvida tem como principio ler a timeline de um usuário e armazenar todos os tweets que chegam para este usuário no período escolhido. Estes tweets serão armazenados em um arquivo, inicialmente, mas no futuro serão associado a um tópico no Apache Kafka.
</p>
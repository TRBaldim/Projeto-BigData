#APACHE FLINK NOTES

<p align="center">
	<a href="https://flink.apache.org/">
		<img src="http://10minbasics.com/wp-content/uploads/2015/10/flink.png">
	</a>
</p>

###Esta sessão do projeto é voltado para notas e dados de como configurar, instalar e rodar a aplicação flink. Todo o projeto Flink ficará nesta pasta.

##Introdução
<p>
	Apache Flink é excelente para garantir processo de dados para os chamados <i> Unbounded DataSets </i> estes modelos definem uma garantia de ser um <a href="https://flink.apache.org/introduction.html#continuous-processing-for-unbounded-datasets">dataset Infinito</a> que será adicionado data continuamente.
</p>
<p>
	Apache Flink permite três grandes garantias de gerenciamento de dados:
	<ul>
		<li> Acurácia - Garante a chegada do dado em sua estrutura mesmo em falha de entrega ou atraso da chegada do dado. </li>
		<li> Tolerante a Falha - Garante recuperação de dados garantindo a manutenção dos dados entregando exatamente uma vez determinado elemento </li>
		<li> Larga Escala - Executa milhares de nós com um gran <i> throughput </i> e com várias caracteristicas de latência </li>
	</ul>
</p>
<p>
	Caracteristicas básicas do apache flink é a garantia da chegada de apenas um elemento, ele consegue garantir a agregaçãoi de dados ou seus dados sumarizados por um certo periodo para garantir um elemento apenas.
</p>
<p align="center">
	<img src="https://flink.apache.org/img/exactly_once_state.png">
</p>
<p>
	Garante uma forma de gerenicamento de Janelas de tempo, garantindo a semantica de eventos por tempo mesmo quando os dados chegam fora de ordem.
</p>
<p align="center">
	<img src="https://flink.apache.org/img/out_of_order_stream.png">
</p>
<p>
	A garantia de tolerancia a falha gera um <i>overhead</i> muito grande de execução da aplicação. O Apache Flink parmite registro dos estados de cada evento de forma rápida e com zero de perde de dados.
</p>
<p align="center">
	<img src="https://flink.apache.org/img/distributed_snapshots.png">
</p>
<p>
	O Flink é capaz de garantir uma alta entrega de dados com baixa latência. Podendo processar milhares de dados de forma mais rápida que concorrentes de streaming como Apache Storm e Apache Spark. Mesmo com <i>Shuffles</i> no processamento.
</p>
<p align="center">
	<img src="https://flink.apache.org/img/streaming_performance.png">
</p>
<p>
	A execução do Apache Flink é voltada a alguns elementos nativos da aplicação, sua estrutura de streaming garante uma execução continua dos dados com pase em suas APIs e Frameworks garantindo execução tanto em uma única JVM como em um cluster local (Yarn ou Mesos) ou na núvem (EC3). O processo do Flink é relacionado a três elemento básicos dentor de seu <a href="https://flink.apache.org/ecosystem.html">ecosistema</a>:
	<ul>
		<li><b>Data Source</b> - Entrada de Dados</li>
		<li><b>Transformation</b> - Transofrmação dos dados pelo Framewrok</li>
		<li><b>Data Sink</b> - Sincronização dos dados com alguma estrutura de aramzenamento</li>
	</ul>
</p>
<p align="center">
	<img src="https://flink.apache.org/img/source-transform-sink-update.png">
</p>

#Instalação

Para a instalação do projeto segue abaixo o link da páigna do projet Apache Flink para a instalação e configuração do ambiente

Instalação - https://ci.apache.org/projects/flink/flink-docs-release-1.2/quickstart/setup_quickstart.html
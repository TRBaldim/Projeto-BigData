#Apache-Kafka

<p align="center">
	<a href="https://kafka.apache.org/">
		<img src="https://kafka.apache.org/images/logo.png">
	</a>
</p>

## Apache-Kafka
<p>
	Utilizaremos o Apache-Kafka neste projeto como uma ferramenta para armazenamento de dados temporários, para não onerar a escrita do dado pela aplicação de entrada <a href="https://github.com/TRBaldim/Projeto-BigData/tree/master/twitter-connection">twitter-connection</a> fazendo uma escrita rápida e de grandes proporções para garantir uma leitura mais eficiente quando for estruturar o dado.
	O Apache-Kafka é uma ferramenta de <i>Streaming</i> de dados, com três capacidades principais:
	<ul>
		<li>Ele permite acessar dados de determinados registros de <i>streaming</i> semelhante a ferramenta de filas de dados empresarias como IBM-MQ</li>
		<li>Ele registra dados em <i>streaming</i> garantindo tolerancia a falha</li>
		<li>Ele permite processar dados em <i>streaming</i> assim que eles ocorram</li>
	</ul>
</p>

##Por que usar Kafka?

<p>
	O Apache-Kafka permite acesso a dados em tempo real, construindo <i>pipelines</i> que permitem acessos de vários meios, vários conectores. Ele permite ações em tempo real de dados para transformação ou reação de dados.
</p>

##Conceitos

<p>
	O Apache-Kafka trabalha com um grupo de conceitos para sua funcionalidade:
	<ul>
		<li>O Kafka trabalha como um cluster, ele pode trabalhar em um ou mais servers</li>
		<li>O cluster do Kafka trabalha com seus registros organizados em tópicos</li>
		<li>Cada registro conciste em uma chave, valor e <i>timestamp</i></li>
	</ul>
</p>

##Componentes

<p>
	O Apache-Kafka trabalha com 4 componentes: <a href="https://kafka.apache.org/documentation.html#producerapi">Producer API</a>, <a href="https://kafka.apache.org/documentation.html#consumerapi">Consumer API</a>, <a href="https://kafka.apache.org/documentation/streams">Stream API</a>, <a href="https://kafka.apache.org/documentation.html#connect">Connector API</a>.
	<ul>
		<li>Producer API - permite publicar streams de dados direto no tópicos do Kafka</li>
		<li>Consumer API - permite uma aplicação a conectar em um dos topicos, e fazer a extração dos dados a medida que eles cheguem</li>
		<li>Stream API - permite a uma aplicação agir como processador de streams, consumindo dados de entrada de um tópico, processando e o escrevendo em outro tópico, muito utilizado para transformação de dados.</li>
		<li>Connector API - Permite utilizar conectores já desenvolvidos para o Apache-Kafka de forma a criar um processo de desenvolvimento de software mais robusto, neste projeto utilizaremos conectores em Python e com o Apache-Flink</li>
	</ul>
</p>

<p align="center">
	<img src="https://kafka.apache.org/0102/images/kafka-apis.png">
</p>
name := "twitter-bigdata"

version := "1.0"

scalaVersion := "2.11.8"

// https://mvnrepository.com/artifact/org.apache.flink/flink-scala_2.11
libraryDependencies += "org.apache.flink" % "flink-scala_2.11" % "1.2.0"
// https://mvnrepository.com/artifact/org.apache.flink/flink-streaming-scala_2.11
libraryDependencies += "org.apache.flink" % "flink-streaming-scala_2.11" % "1.2.0"
// https://mvnrepository.com/artifact/org.apache.flink/flink-clients_2.11
libraryDependencies += "org.apache.flink" % "flink-clients_2.11" % "1.2.0"
// https://mvnrepository.com/artifact/org.apache.flink/flink-connector-twitter_2.11
libraryDependencies += "org.apache.flink" % "flink-connector-twitter_2.11" % "1.2.0"

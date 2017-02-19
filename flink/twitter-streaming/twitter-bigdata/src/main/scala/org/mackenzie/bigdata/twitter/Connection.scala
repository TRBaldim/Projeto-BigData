package org.mackenzie.bigdata.twitter

/**
  * Created by thiago on 19/02/17.
  * Example of: https://goo.gl/bmSD0J
  */
import java.util.Properties

import org.apache.flink.api.scala._
import org.apache.flink.streaming.connectors.twitter._
import org.apache.flink.api.java.utils.ParameterTool
import org.apache.flink.streaming.api.scala.StreamExecutionEnvironment
import com.twitter.hbc.core.endpoint.{StatusesFilterEndpoint, StreamingEndpoint}
import org.apache.flink.streaming.api.windowing.time.Time

import scala.collection.JavaConverters._

// val chicago = new Location(new Location.Coordinate(-86.0, 41.0), new Location.Coordinate(-87.0, 42.0))

//////////////////////////////////////////////////////
// Create an Endpoint to Track our terms
class myFilterEndpoint extends TwitterSource.EndpointInitializer with Serializable {
  @Override
  def createEndpoint(): StreamingEndpoint = {
    val endpoint = new StatusesFilterEndpoint()
    //endpoint.locations(List(chicago).asJava)
    endpoint.trackTerms(List("odebrecht", "lava", "jato").asJava)
    endpoint
  }
}

object Connection {
  def main(args: Array[String]): Unit = {

    val props = new Properties()

    val params: ParameterTool = ParameterTool.fromArgs(args)
    val env = StreamExecutionEnvironment.getExecutionEnvironment

    env.getConfig.setGlobalJobParameters(params)
    env.setParallelism(params.getInt("parallelism", 1))

    if (params.has("consumer-key")) {
      props.setProperty(TwitterSource.CONSUMER_KEY, params.get("consumer-key"))
    }

    if (params.has("private-key")) {
      props.setProperty(TwitterSource.CONSUMER_SECRET, params.get("consumer-key"))
    }

    if (params.has("token")) {
      props.setProperty(TwitterSource.TOKEN, params.get("token"))
    }
    if (params.has("token-secret")) {
      props.setProperty(TwitterSource.TOKEN_SECRET, params.get("token-secret"))
    }
    val source = new TwitterSource(props)
    val epInit = new myFilterEndpoint()

    source.setCustomEndpointInitializer(epInit)

    val streamSource = env.addSource(source)

    streamSource.map(s => (0,1))
      .keyBy(0)
      .timeWindow(Time.minutes(2), Time.seconds(30))
      .sum(1)
      .map(t => t._2)
      .writeAsText(params.get("output"))

    env.execute("Twitter Count")
  }
}

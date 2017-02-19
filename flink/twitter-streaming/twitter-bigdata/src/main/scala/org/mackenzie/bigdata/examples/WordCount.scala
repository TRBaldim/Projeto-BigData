package org.mackenzie.bigdata.examples

/**
  * Created by thiago on 18/02/17.
  */
import org.apache.flink.api.java.utils.ParameterTool
import org.apache.flink.api.scala._

object WordCount {
  def main(args: Array[String]): Unit = {
    val params : ParameterTool = ParameterTool.fromArgs(args)

    val env = ExecutionEnvironment.getExecutionEnvironment

    env.getConfig.setGlobalJobParameters(params)
    val text = env.readTextFile(params.get("input"))

    val counts = text.flatMap { _.toLowerCase.split("\\W+") filter { _.nonEmpty } }
      .map{ (_, 1) }
      .groupBy(0)
      .sum(1)

    if (params.has("output")) {
      counts.writeAsCsv(params.get("output"), "\n", " ")
      env.execute("Scala WordCount Example")
    } else {
      println("Printing Results")
      counts.print()
    }


  }
}

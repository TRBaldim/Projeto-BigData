package org.mackenzie.bigdata.examples

/**
  * Created by thiago on 18/02/17.
  */

import org.apache.flink.api.java.utils.ParameterTool
import org.apache.flink.api.scala._
import org.apache.flink.util.Collector

object ConnectedComponents {
  def getVertexDataSet(env: ExecutionEnvironment, params: ParameterTool): DataSet[Long] = {
    if (params.has("vertices")) {
      env.readCsvFile[Tuple1[Long]](params.get("vertices"), includedFields = Array(0)).map { x => x._1 }
    }
    else {
      println("Executing ConnectedComponents example with default vertices data set.")
      println("Use --vertices to specify file input.")
      env.readCsvFile[Tuple1[Long]](params.get("vertices"), includedFields = Array(0)).map { x => x._1 }
    }
  }

  def getEdgeDataSet(env: ExecutionEnvironment, params: ParameterTool):
  DataSet[(Long, Long)] = {
    if (params.has("edges")) {
      env.readCsvFile[(Long, Long)](
        params.get("edges"),
        fieldDelimiter = " ",
        includedFields = Array(0, 1))
        .map { x => (x._1, x._2) }
    }
    else {
      println("Executing ConnectedComponents example with default edges data set.")
      println("Use --edges to specify file input.")
      env.readCsvFile[(Long, Long)](
        params.get("edges"),
        fieldDelimiter = " ",
        includedFields = Array(0, 1))
        .map { x => (x._1, x._2) }
    }
  }

  def main(args: Array[String]): Unit = {

    val params = ParameterTool.fromArgs(args)
    val env = ExecutionEnvironment.getExecutionEnvironment
    val maxIterations: Int = params.getInt("iterations", 10)

    env.getConfig.setGlobalJobParameters(params)

    val vertices = getVertexDataSet(env, params).map { id => (id, id) }.withForwardedFields("*->_1;*->_2")

    val edges = getEdgeDataSet(env, params).flatMap { edge => Seq(edge, (edge._2, edge._1)) }

    val verticesWithComponents = vertices.iterateDelta(vertices, maxIterations, Array("_1")) {
      (s, ws) =>

      val allNeighbors = ws.join(edges).where(0).equalTo(0) { (vertex, edge) =>
        (edge._2, vertex._2) }.withForwardedFieldsFirst("_2->_2").withForwardedFieldsSecond("_2->_1")

      val minNeighbors = allNeighbors.groupBy(0).min(1)

      // update if the component of the candidate is smaller
      val updatedComponents = minNeighbors.join(s).where(0).equalTo(0) {
        (newVertex, oldVertex, out: Collector[(Long, Long)]) =>
          if (newVertex._2 < oldVertex._2) out.collect(newVertex)
      }.withForwardedFieldsFirst("*")

      // delta and new workset are identical
      (updatedComponents, updatedComponents)

    }
    if (params.has("output")) {
      verticesWithComponents.writeAsCsv(params.get("output"), "\n", " ")
      env.execute("Scala Connected Components Example")
    } else {
      println("Printing result to stdout. Use --output to specify output path.")
      verticesWithComponents.print()
    }

  }
}

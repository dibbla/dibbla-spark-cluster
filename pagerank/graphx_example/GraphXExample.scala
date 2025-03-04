import org.apache.spark._
import org.apache.spark.graphx._
import org.apache.spark.graphx.GraphLoader
import org.apache.spark.sql.SparkSession

object GraphXExample {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder
      .appName("GraphXExample")
      .master("local[*]")
      .getOrCreate()
    val sc = spark.sparkContext

    // Load the graph from an edge list file
    val graph = GraphLoader.edgeListFile(sc, "edges.txt")

    // Run PageRank algorithm
    val ranks = graph.pageRank(0.01).vertices

    // Load vertices with names (assuming CSV format: "vertexId,name")
    val users = sc.textFile("vertices.txt").map { line =>
      val fields = line.split(",")
      (fields(0).toLong, fields(1))
    }

    // Join the user names with their PageRank scores
    val rankedNames = users.join(ranks).map {
      case (id, (name, rank)) => (name, rank)
    }

    // Print the PageRank results
    println("PageRank Results:")
    rankedNames.collect().foreach { case (name, rank) =>
      println(s"$name: $rank")
    }
    
    spark.stop()
  }
}

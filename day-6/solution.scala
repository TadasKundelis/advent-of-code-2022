import scala.io.Source

object Solution extends App {
  val input = Source.fromFile("./input.txt").toList

  println(solve(input, size = 4) == 1356)
  println(solve(input, size = 14) == 2564)

  def solve(input: List[Char], size: Int): Int = {
    input
      .sliding(size)
      .zipWithIndex
      .find { case (group, index) => group.distinct == group }
      .map(_._2)
      .get + size
  }
}
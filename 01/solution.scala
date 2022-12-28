import scala.io.Source
import scala.math._

object Solution extends App {
  val input = Source.fromFile("./01/input.txt").mkString.split("\n\n").map(_.split("\n").map(_.toInt))
  val sortedSums = input.map(_.sum).sorted(Ordering.Int.reverse)
  val part1 = sortedSums.head
  val part2 = sortedSums.take(3).sum

  println(part1 == 68787)
  println(part2 == 198041)
}

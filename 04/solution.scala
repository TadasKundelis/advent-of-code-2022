import scala.io.Source
import scala.util.matching.Regex


object Solution extends App {
  val lines = Source.fromFile("./input.txt").getLines
    .map(s => ("\\d+".r).findAllIn(s).map(_.toInt).toList)
    .toList

  println(solve(lines, predicatePart1) == 582)
  println(solve(lines, predicatePart2) == 893)

  def unpackList(nums: List[Int]): (Int, Int, Int, Int) = nums match {
    case List(a, b, c, d) => (a, b, c, d)
  }

  def predicatePart1(a: Int, b: Int, c: Int, d: Int): Boolean = (a >= c && b <= d) || (a <= c && b >= d)

  def predicatePart2(a: Int, b: Int, c: Int, d: Int): Boolean = c <= b && a <= d

  def solve(lines: List[List[Int]], predicate: ((Int, Int, Int, Int)) => Boolean): Int = {
    lines.map(unpackList).filter(predicate).size
  }
}
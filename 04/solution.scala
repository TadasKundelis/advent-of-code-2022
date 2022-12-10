import scala.io.Source
import scala.util.matching.Regex


object Solution extends App {
  val lines = Source.fromFile("./input.txt").getLines
    .map(s => ("\\d+".r).findAllIn(s).map(_.toInt).toList)
    .toList

  println(solvePart1(lines) == 582)
  println(solvePart2(lines) == 893)

  def predicatePart1(nums: List[Int]): Boolean = {
    val a :: b :: c :: d :: Nil = nums
    (a >= c && b <= d) || (a <= c && b >= d)
  }

  def predicatePart2(nums: List[Int]): Boolean = {
    val a :: b :: c :: d :: Nil = nums
    c <= b && a <= d
  }

  def solvePart1(lines: List[List[Int]]): Int = lines.filter(predicatePart1).size

  def solvePart2(lines: List[List[Int]]): Int = lines.filter(predicatePart2).size
}
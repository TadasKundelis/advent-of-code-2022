import scala.io.Source

object Solution extends App {
  val lines = Source.fromFile("./input.txt").getLines.toList
  val lowerCaseLetters = "abcdefghijklmnopqrstuvwxyz"
  val letters = s" ${lowerCaseLetters}${lowerCaseLetters.toUpperCase}"

  println(solvePart1(lines) == 7875)
  println(solvePart2(lines) == 2479)

  def findCommonCharPart1(line: String): Char = {
    val mid = line.length / 2
    val (firstHalf, secondHalf) = (line.slice(0, mid), line.slice(mid, mid * 2))
    firstHalf.toSet.intersect(secondHalf.toSet).head
  }

  def solvePart1(lines: List[String]): Int = {
    lines
      .map(findCommonCharPart1)
      .map(c => letters.indexOf(c))
      .sum
  }

  def findCommonCharPart2(lines: List[String]): Char = {
    lines.map(_.toSet).reduce(_ intersect _).head
  }

  def solvePart2(lines: List[String]): Int = {
    lines
      .grouped(3)
      .map(findCommonCharPart2)
      .map(c => letters.indexOf(c))
      .sum
  }
}
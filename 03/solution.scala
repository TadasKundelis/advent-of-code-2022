import scala.io.Source

object Solution extends App {
  val lines = Source.fromFile("./input.txt").getLines.toList
  val lowerCaseLetters = "abcdefghijklmnopqrstuvwxyz"
  val letters = s" $lowerCaseLetters${lowerCaseLetters.toUpperCase}"

  println(solvePart1(lines) == 7875)
  println(solvePart2(lines) == 2479)

  def splitLine(line: String): List[String] = {
    List(line.slice(0, line.length / 2), line.slice(line.length / 2, line.length))
  }

  def findCommonChar(lists: List[String]): Char = lists.map(_.toSet).reduce(_ intersect _).head

  def countSumOfCommonChars(lists: List[List[String]]): Int = {
    lists.map(findCommonChar).map(c => letters.indexOf(c)).sum
  }

  def solvePart1(lines: List[String]): Int = countSumOfCommonChars(lines.map(splitLine))

  def solvePart2(lines: List[String]): Int = countSumOfCommonChars(lines.grouped(3).toList)
}
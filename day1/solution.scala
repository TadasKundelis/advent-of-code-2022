import scala.io.Source
import scala.math._

object Solution extends App {
  val nums = Source.fromFile("./input.txt").getLines.toList

  def sumCaloriesPerElf(calories: List[String], currSum: Int = 0, numLists: List[Int] = List.empty): List[Int] = calories match {
      case Nil => numLists
      case head :: tail if head.isEmpty => sumCaloriesPerElf(tail, currSum = 0, numLists :+ currSum)
      case head :: tail => sumCaloriesPerElf(tail, currSum + head.toInt, numLists)
  }

  def solvePart1(nums: List[String]): Int = sumCaloriesPerElf(nums).max

  def solvePart2(nums: List[String]): Int = {
    sumCaloriesPerElf(nums)
      .sorted(Ordering.Int.reverse)
      .take(3)
      .sum
  }

  println(solvePart1(nums) == 68787)
  println(solvePart2(nums) == 198041)
}

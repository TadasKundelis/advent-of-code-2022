import scala.io.Source

object Solution extends App {
  val lines = Source.fromFile("./input.txt").getLines.map(_.split(" ").toList).toList

  println(solvePart1(lines) == 14780)
  println(solvePart2(lines))

  def solvePart1(lines: List[List[String]]): Int = {
    val valuesByCycle = resolveValuesForCycles(lines)
    signalStrengthSum(valuesByCycle)
  }

  def solvePart2(lines: List[List[String]]): String = {
    val valuesByCycle = resolveValuesForCycles(lines)
    val pixels = valuesByCycle.zipWithIndex.foldLeft(List.empty) { case (pixels, (value, index)) =>
      if (spritePositions(value).contains(index % 40)) pixels :+ "#" else pixels :+ "."
    }
    pixels.grouped(40).map(_.mkString).mkString("\n")
  }

  def spritePositions(value: Int): List[Int] = List(value - 1, value, value + 1)

  def signalStrengthSum(numsByCycle: List[Int]): Int = {
    (19 to 239 by 40).map(index => (index + 1) * numsByCycle(index)).sum
  }

  def resolveValuesForCycles(lines: List[List[String]]): List[Int] = {
    lines.foldLeft((List.empty[Int], 1)) { case ((valuesByCycle, lastValue), line) =>
      val newValuesByCycle = valuesByCycle :+ lastValue
      line match {
        case command :: numFromInput :: Nil => (newValuesByCycle :+ lastValue, lastValue + numFromInput.toInt)
        case _ => (newValuesByCycle, lastValue)
      }
    }
  }._1
}
import scala.io.Source

object Solution extends App {
  val lines = Source.fromFile("./input.txt").getLines.toList.map(l => (l.head, l.last))

  val draw = Map[Char, Char](
    'A' -> 'X',
    'B' -> 'Y',
    'C' -> 'Z',
  )

  val winning = Map[Char, Char](
    'C' -> 'X',
    'B' -> 'Z',
    'A' -> 'Y',
  )

  val losing = Map[Char, Char](
    'C' -> 'Y',
    'B' -> 'X',
    'A' -> 'Z',
  )

  val pointsForOutcome = Map[Char, Int](
    'X' -> 0,
    'Y' -> 3,
    'Z' -> 6,
  )

  val pointsForChoice = Map[Char, Int](
    'X' -> 1,
    'Y' -> 2,
    'Z' -> 3,
  )

  def pointsForGamePart1 (line: (Char, Char)): Int = {
    val (hisChoice, myChoice) = line
    val points = pointsForChoice(myChoice)
    val additional = {
      if (winning(hisChoice) == myChoice) 6
      else if (draw(hisChoice) == myChoice) 3
      else 0
    }
    points + additional
  }

  def solvePart1(lines: List[(Char, Char)]): Int = {
    lines.map(pointsForGamePart1).sum
  }

  def resolveMyChoice(hisChoice: Char, outCome: Char): Char = {
    val mapping = Map(
      'X' -> losing(hisChoice),
      'Y' -> draw(hisChoice),
      'Z' -> winning(hisChoice)
    )

    mapping(outCome)
  }

  def pointsForGamePart2(line: (Char, Char)): Int = {
    val (hisChoice, outCome) = line
    val points = pointsForOutcome(outCome)
    val myChoice = resolveMyChoice(hisChoice, outCome)
    points + pointsForChoice(myChoice)
  }

  def solvePart2(lines: List[(Char, Char)]): Int = {
    return lines.map(pointsForGamePart2).sum
  }

  println(solvePart1(lines) == 15523)
  println(solvePart2(lines) == 15702)
}
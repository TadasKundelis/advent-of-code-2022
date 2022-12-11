import scala.io.Source
import scala.math._
import scala.util.matching.Regex.Match

case class Monkey(
  number: Int, 
  items: List[Int], 
  operation: (BigInt) => BigInt, 
  resolveNextMonkey: (Int) => Int,
  inspectedCount: BigInt = 0) {

  def incrementInspectedCount(): Monkey = {
    this.copy(inspectedCount = this.inspectedCount + 1)
  }
}

object Monkey {
  def resolveOperation(regexMatch: Match): (Option[BigInt], BigInt) => BigInt = regexMatch.group(3).mkString match {
    case v if v == "+" => (a: Option[BigInt], b: BigInt) => a.getOrElse(b) + b
    case v if v == "*" => (a: Option[BigInt], b: BigInt) => (a.getOrElse(b) * b) % 9699690
  }

  def createNextMonkeyResolver(regexMatch: Match): (Int) => Int = {
    val divider = regexMatch.group(5).toInt
    val destinationIfTrue = regexMatch.group(6).toInt
    val destinationIfFalse = regexMatch.group(7).toInt 
    (num: Int) => if (num % divider == 0) destinationIfTrue else destinationIfFalse
  }

  def resolveItems(regexMatch: Match): List[Int] = {
    regexMatch.group(2).split(",").map(s => s.trim().toInt).toList
  }

  def resolveOperand(regexMatch: Match): Option[BigInt] = {
    val value = regexMatch.group(4).toString
    if (value == "old") None 
    else Some(BigInt(value)) 
  }


  def apply(monkeyStr: String): Monkey = {
    val pattern = """Monkey (\d+):\W+Starting items: ([^\n]+)\W+Operation: new = old ([+*-\\]) (\w+)\W+Test: divisible by (\d+)\W+If true: throw to monkey (\d+)\W+If false: throw to monkey (\d+)""".r

    pattern.findFirstMatchIn(monkeyStr).map {m =>
        val monkeyNumber = m.group(1).toInt
        val items = resolveItems(m)
        val operand = resolveOperand(m)
        val operation = resolveOperation(m)
        val resolveNextMonkey = createNextMonkeyResolver(m)
        Monkey(monkeyNumber, items, operation(operand, _), resolveNextMonkey)
    }.get
  }
}

object Solution extends App {
  val monkeyStrings = Source.fromFile("./input.txt").mkString.split("\\n\\n").toList
  var monkeys = monkeyStrings.map(Monkey.apply).toArray

  for (_ <- 1 to 10000) {
    for (j <- monkeys.indices) {
      val monkey = monkeys(j)
      for (item <- monkey.items) {
        val updatedItem = monkey.operation(item).toInt
        monkeys(j) = monkeys(j).copy(inspectedCount = monkeys(j).inspectedCount + 1)
        val nextMonkey = monkey.resolveNextMonkey(updatedItem).toInt
        val currentItems = monkeys(nextMonkey).items
        monkeys(nextMonkey) = monkeys(nextMonkey).copy(items = currentItems :+ updatedItem)
      }
      monkeys(j) = monkeys(j).copy(items = List.empty)
    }
  }
  println(monkeys.map(_.inspectedCount).sorted.toList.takeRight(2).reduce(_ * _))

}
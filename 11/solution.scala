import scala.io.Source
import scala.math._

case class Monkey(
                   number: BigInt, items: List[BigInt], operation: (BigInt) => BigInt, resolveNextMonkey: (BigInt) => BigInt, inspectedCount: BigInt = 0) {

  def incrementInspectedCount(): Monkey = {
    this.copy(inspectedCount = this.inspectedCount + 1)
  }
}

object Monkey {
  def resolveOperation(input: String): Option[BigInt] => BigInt => BigInt = {
    def sum(a: Option[BigInt])(b: BigInt): BigInt = a.getOrElse(b) + b

    def subtract(a: Option[BigInt])(b: BigInt): BigInt = (a.getOrElse(b) - b)

    def multiply(a: Option[BigInt])(b: BigInt): BigInt = (a.getOrElse(b) * b) % 9699690 // remove hardcoded value

    val operations = Map(
      "+" -> sum,
      "-" -> subtract,
      "*" -> multiply,
    )

    operations(input)
  }

  def apply(monkeyStr: String): Monkey = {
    val pattern = """Monkey (\d+):\W+Starting items: ([^\n]+)\W+Operation: new = old ([+*-\\]) (\w+)\W+Test: divisible by (\d+)\W+If true: throw to monkey (\d+)\W+If false: throw to monkey (\d+)""".r

    pattern.findFirstMatchIn(monkeyStr).map {
      m =>
        val monkeyNumber = BigInt(m.group(1))
        val items = m.group(2).mkString.split(",").map(_.trim()).map(s => BigInt(s)).toList
        val operand = if (m.group(4).toString == "old") None else Some(BigInt(m.group(4)))
        val divider = BigInt(m.group(5))
        val operation = resolveOperation(m.group(3).mkString)
        val destinationIfTrue = m.group(6)
        val destinationIfFalse = m.group(7)
        val resolveNextMonkey = (num: BigInt) => {
          if (num % divider == 0) BigInt(destinationIfTrue)
          else BigInt(destinationIfFalse)
        }
        Monkey(monkeyNumber, items, operation(operand), resolveNextMonkey)
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
        val updatedItem = monkey.operation(item)
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
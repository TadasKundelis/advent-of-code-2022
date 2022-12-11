import scala.io.Source
import scala.math._

case class Monkey(number: Int, items: List[Int], operation: (Int) => Int, resolveNextMonkey: (Int) => Int, inspectedCount: Int = 0) {

  def incrementInspectedCount(): Monkey = {
    this.copy(inspectedCount = this.inspectedCount + 1)
  }
}

object Monkey {
  def resolveOperation(input: String): Option[Int] => Int => Int = {
    def sum(a: Option[Int])(b: Int): Int = a.getOrElse(b) + b

    def subtract(a: Option[Int])(b: Int): Int = a.getOrElse(b) - b

    def multiply(a: Option[Int])(b: Int): Int = a.getOrElse(b) * b

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
        val monkeyNumber = m.group(1).toInt
        val items = m.group(2).mkString.split(",").map(_.trim()).map(_.toInt).toList
        val operation = resolveOperation(m.group(3).mkString)
        val operand = if (m.group(4).toString == "old") None else Some(m.group(4).toInt)
        val divider = m.group(5).toInt
        val destinationIfTrue = m.group(6)
        val destinationIfFalse = m.group(7)
        val resolveNextMonkey = (num: Int) => {
          if (num % divider == 0) destinationIfTrue.toInt
          else destinationIfFalse.toInt
        }
        Monkey(monkeyNumber, items, operation(operand), resolveNextMonkey)
    }.get
  }
}

object Solution extends App {
  val monkeyStrings = Source.fromFile("./input.txt").mkString.split("\\n\\n").toList
  var monkeys = monkeyStrings.map(Monkey.apply).toArray

  for (i <- 1 to 20) {
    for (j <- 0 until monkeys.size) {
      val monkey = monkeys(j)
//      println("XXX")
//      println(monkey.number)
//      println(monkey.items)
      for (item <- monkey.items) {
        val updatedItem = floor((monkey.operation(item) / 3).toDouble).toInt
//        println(j)
//        println(s"original item ${item}")
//        println(s"updated item ${updatedItem}")
        monkeys(j) = monkeys(j).copy(inspectedCount = monkeys(j).inspectedCount + 1)
        val nextMonkey = monkey.resolveNextMonkey(updatedItem)
//        println(s"next monkey ${nextMonkey}")
        val currentItems = monkeys(nextMonkey).items
        monkeys(nextMonkey) = monkeys(nextMonkey).copy(items = currentItems :+ updatedItem)
      }
      monkeys(j) = monkeys(j).copy(items = List.empty)
    }
  }

  print(monkeys.map(_.inspectedCount).sorted.toList.takeRight(2).reduce(_ * _))

}
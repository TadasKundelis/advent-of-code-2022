import scala.io.Source
import scala.math._

object Solution extends App {
  val matrix = Source.fromFile("08/input.txt").getLines.toList.map(_.toList.map(_.toString.toInt))

  val getMaxElement = (acc: List[Int], curr: Int) => acc :+ max(acc.last, curr)
  val getMaxElementsFromLeft = (row: List[Int]) => row.drop(1).foldLeft(List(row.head))(getMaxElement)

  val maxFromLeft = matrix.map(getMaxElementsFromLeft)
  val maxFromRight = matrix.map(_.reverse).map(getMaxElementsFromLeft).map(_.reverse)
  val maxFromTop = matrix.transpose.map(getMaxElementsFromLeft)
  val maxFromBottom = matrix.transpose.map(_.reverse).map(getMaxElementsFromLeft).map(_.reverse)

  val res = matrix.zipWithIndex.map { case (row, rowIndex) =>
    row.zipWithIndex.count { case (value, colIndex) =>
      val seenFromLeft = if (colIndex > 0) maxFromLeft(rowIndex)(colIndex - 1) < value else true
      val seenFromRight = if (colIndex < row.size - 1) maxFromRight(rowIndex)(colIndex + 1) < value else true
      val seenFromTop = if (rowIndex > 0) maxFromTop(colIndex)(rowIndex - 1) < value else true
      val seenFromBottom = if (rowIndex < matrix.size - 1) maxFromBottom(colIndex)(rowIndex + 1) < value else true
      seenFromLeft || seenFromRight || seenFromTop || seenFromBottom
    }
  }.sum

  print(res == 1693)
}
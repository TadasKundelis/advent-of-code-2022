import scala.io.Source
import scala.math._

object Solution extends App {
  val matrix = Source.fromFile("08/input.txt").getLines.toList.map(_.toList.map(_.toString.toInt))

  type Matrix[T] = List[List[T]]

  val getMaxElementsFromLeft = (row: List[Int]) => {
    val rollingMax = row.scanLeft(-1) { case (acc, curr) => max(acc, curr) }.init
    rollingMax.zip(row).map { case (max, curr) => max < curr }
  }

  val maxFromLeft = matrix.map(getMaxElementsFromLeft)
  val maxFromRight = matrix.map(_.reverse).map(getMaxElementsFromLeft).map(_.reverse)
  val maxFromTop = matrix.transpose.map(getMaxElementsFromLeft).transpose
  val maxFromBottom = matrix.transpose.map(_.reverse).map(getMaxElementsFromLeft).map(_.reverse).transpose

  def mergeMatrices(matrices: Matrix[Boolean]*): Matrix[Boolean] = matrices.reduce {
    case (matrix1, matrix2) => matrix1.zip(matrix2).map((xs, ys) => xs.zip(ys).map((x, y) => x || y))
  }

  val res = mergeMatrices(maxFromLeft, maxFromRight, maxFromBottom, maxFromTop).flatten.count(_ == true)
  print(res == 1693)
}

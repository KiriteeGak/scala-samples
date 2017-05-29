/**
  * Created by kiritee on 29/5/17.
  */
object pascalsTriangle {
  def permutation(n:Int):Int = {
    n match {
      case 0 => 1
      case 1 => 1
      case _ => n*permutation(n-1)
      }
    }

  def main(args: Array[String]): Unit = {
    val root: Int = 4
    for (i <- 0 to root){println(permutation(root)/(permutation(root-i)*permutation(i)))}
  }
}

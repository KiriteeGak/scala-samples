/**
  * Created by kiritee on 29/5/17.
  */
object fibbonaci {

  def fibbonaci(n:Int):Int = {
    n match {
      case 0 => 0
      case 1 => 1
      case _ => n+fibbonaci(n-1)
    }
  }

  def main(args: Array[String]): Unit = {
    println(fibbonaci(10))
  }
}

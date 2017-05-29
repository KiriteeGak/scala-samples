/**
  * Created by kiriteegak on 15/4/17.
  */
object traitsExtension {

  trait s{
    val somval = 3
    def f(x:String) = x.concat(" <3")
  }

  trait m extends s{
    override val somval = 5
    def f1(x:Int) = x+2
  }
  class p extends m with s

  def main(args: Array[String]): Unit = {
    val instance1 = new p
    println(instance1.f("Polo"))
    println(instance1.f1(5))
    println(instance1.somval)
  }
}
/**
  * Created by kiriteegak on 28/5/17.
  */
object stringRepresentations {
  val string: String = "abbbbccd"
  val stringList: List[String] = string.split("").toList
  var count = 1
  var returnString: String = ""
  def main(args: Array[String]): Unit = {
    for ((character, index) <- stringList.zipWithIndex){
     if (index != stringList.length-1){
       if (character == stringList(index+1)){count += 1}
       else {
         if (count != 1){returnString = returnString.concat(character).concat(count.toString); count = 1}
         else {returnString = returnString.concat(character)}
         count = 1
       }
     }
     else {
       if (count != 1){returnString = returnString.concat(character).concat(count.toString)}
       else {returnString = returnString.concat(character)}
     }
    }
    println(returnString)
  }
}
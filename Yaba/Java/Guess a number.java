/**
     * 1) Akanbi Rasaq Oluwaseun 09057456380,
     * 2) Ideh Constance Tessy 08039195572
     * 3) Mfon Ankoh  07066789934
     * 4) Abejoye Oluwajimi E.  08095723973
     * 5)Achigonye chinaemerem 09023047431
     * @param args the command line arguments
     */
package javaproject;
import java.util.*;
/**
 *
 * 
 */
public class Javaproject {

    
    public static void main(String[] args) {
         System.out.println("Welcome guess the number");
       Random rand = new Random();
       int a = rand.nextInt(10)+3;
       for(int i = 0; i <10; i++){
       System.out.println("Guess a number between 3 and 12");
       Scanner input = new Scanner(System.in);
       int b = input.nextInt();
       if(b==a){
           System.out.println("thumbs up");
           break;
       }
       else{
           System.out.println("booooo");
       }
           
    }
    System.out.println("the guess number is "+a);
}
}

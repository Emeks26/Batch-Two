/* Chalse Nicholas nck@usa.com
Bala yakubu   yakububala51@gmail.com
Adebayo Adebola Helen - adebayoadebola9@gmail.com
Adebayo Muibat Adedoyin- adebayomuibat@gmail.com 
Oyewusi Oluwasesan Gabriel- oyewusisesan@gmail.com



*/
package hangman;
import java.util.*;

public class HangMan {
    private static Random genWords = new Random ();
    private static Scanner userInput = new Scanner (System.in);
    public static String[] listOfWords = {"Congratulation","Dongratulation","Eongratulation","Fongratulation","Gongratulation","Hongratulation","Iongratulation","Jongratulation","Kongratulation","Longratulation"};
    public static void main(String[] args) {
       String dash = ""; 
       String dash1 = ""; 
       String [] dashArr = dash.split("") ;
 
        int index = genWords.nextInt(10);
        String word = listOfWords[index];
        for(int i =0; i < word.length() ; i++){
            dash += "-";
        
        }
         System.out.println("Please enter your name to play:");
        String name = userInput.nextLine();
        System.out.println("Welcome " +name +"  You are ready to play");
        System.out.println(dash);
        
        for(int j = 0 ; j < word.length(); j++){
            System.out.println("Guess a letter");
            String guess = userInput.next();
            dashArr = dash.split("");
            for(int i = 0 ; i < word.length(); i++){
                if(word.split("")[i].equals(guess)){
                          dashArr[i] = guess;
                }
            }
            dash1="";
            for(int k = 0 ; k < word.length(); k++){
                dash1 += dashArr[k]; 
            }
            dash = dash1;
            System.out.println(dash1);
        
        }
       
       
       
    }
    
}

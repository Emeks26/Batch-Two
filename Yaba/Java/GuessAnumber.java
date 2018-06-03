/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package guessanumber;
import java.util.Random;
import java.util.Scanner;
/**
 *
 * @author pi
 */
public class GuessAnumber {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        //students, moronke oluwatoyin,omotayo omoyemi, jude ojogwu
        Random guess = new Random(); 
        
        Scanner input = new Scanner(System.in);
        int i;
        int randValue= rand.nextInt(12);
        
          for(int  i=0; i < 13;i++){
              System.out.println("Guess the no");
        if(int guess== randValue){ 
        System.out.println("Correct");
        break;
          }
        else{
                System.out.println("Wrong Try Again");
                
        
    }
              System.out.println("The answer is" +randValue);
        
            
        }
        
        
   
                
        
                
        
    }
    
}

/*
 *1)Ejike Ekene 08182875713
 *2)James Dayo 08090639352
 *3)Oramasionwu Samuel 07054052155 
 */
package guess.the.number;
import java.util.Scanner;
import java.util.Random;
/**
 *
 * @author Alexander
 */
public class GuessTheNumber {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int guess,i;
        Scanner input = new Scanner(System.in);
       
        Random rand = new Random();
        
        int randValue = rand.nextInt(11);
        
       
        for(i =0; i<5; i+=1){
        System.out.println("Guess the number between 0 to 10");
        guess = input.nextInt();
        if(guess == randValue){
            System.out.println("Correct");
            break;
        }
        
        else{
            System.out.println("Try again");
        }
            
        }
        
        System.out.println("The guess number is"+   randValue);
    } 
        
        
        
        
        
    }
    

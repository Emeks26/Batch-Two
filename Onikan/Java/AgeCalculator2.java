/*
 * Project Name: Age Calculator based on Shoe Size
 *
 * Team Members: 
 * Ogabiyi Abayomi, 08132350042, yogabiyi@yahoo.com

 */
package agecalculator2;
import java.util.Scanner;
/**
 *
 * @author CodeLagos Onikan Center
 */
public class AgeCalculator2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner age = new Scanner(System.in);
        System.out.println("Am about to tell you your AGE!!!");
        System.out.println(" Add 5 to your AGE");
        System.out.println("press 1 to proceed");
        int Input1;
Input1 = age.nextInt();
switch (Input1){
    case 1:
        System.out.println("Multiply your answer by 4");
        System.out.println("press 1 to proceed");
        int input2;
        input2 = age.nextInt();
        switch (input2){
    case 1:
        System.out.println("Divide your answer by 2 "
                + "and enter your answer");
      int ans;
        ans = age.nextInt();
        System.out.println( "You are " + ( (ans*2)/4-5 ) +  " years old" ) ;
}
}
    }
    
}

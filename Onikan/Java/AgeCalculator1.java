/*
 * Project Name: Age Calculator based on Shoe Size
 *
 * Team Members: 
 * Akeju Osuolale, 07038243809, olaposiakeju@gmail.com

 */
package agecalculator1;
import java.util.Scanner;

/**
 *
 * @author CodeLagos Onikan Center
 */
public class AgeCalculator1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner shoesize = new Scanner(System.in);
        int size, Ans, Ans2, Ans3, Ans4, birthyear;
        System.out.println("Enter your shoe size");
        size = shoesize.nextInt();
        System.out.println("Enter your year of birth");
        birthyear = shoesize.nextInt();
        Ans = (size * 5) + 50;
        Ans2 = (Ans *20) + 1018;
        Ans3 = Ans2 - birthyear;
        Ans4 = Ans3 - (size * 100);
        System.out.println(Ans3);
        System.out.println("The first two digits represent your shoe size while the other two gigits represent your age");
    }
    
}

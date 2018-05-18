/*
 * Project Name: Body Mass Index Calculator
 *
 * Team Members: 
 * Olufemi Olomitutu, 07062311779, faginorish@gmail.com
 * Akeju Osuolale, 07038243809, olaposiakeju@gmail.com
 * Foluke Olufemi, 09051691752, femioluwole63@yahoo.com
 * Ogabiyi Abayomi,	08132350042, yogabiyi@yahoo.com
 * Ishola Rasheed, 08038340875, ishowtech001@gmail.com
 * Kabir Salam, 07069495725, salamkabirdolapo@gmail.com
 * Olasunkanmi Taiwo, 08068547415, taiwoolasunkanmi75@yahoo.com
 */
package bmi;
import java.util.Scanner;

/**
 *
 * @author CodeLagos Onikan Center
 */
public class BMI {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input = new Scanner(System.in);
		double weight = 0.0;
		double height = 0.0;
		double Height = 0.0;
		double FinalHeight = 0.0;
		double bmi = 0.0;
		
		// TODO Auto-generated method stub
		System.out.println("This is Body Mass Index Calculator \nCreated by OLOMITUTU OLUFEMI\n-----------------------------------");
System.out.println("Please Enter your weight in Kilogram:");
weight = input.nextDouble();
//This get user's weight in kilogram

System.out.println("Please Enter Your Height in Centimeter:");
height = input.nextDouble();
//this get user's height
Height = height/100;
FinalHeight = Height * Height;
//this converts height ti m2
bmi = weight / FinalHeight;
System.out.println("Your BMI is " + bmi + "Kg/m2");
if (bmi > 25 ) {
	System.out.println("You're at Risk");
}else {
	System.out.println("You're Healthy");
}
    }
    
}

/*
 * Project Name: Area of Shapes calculator done during the class session
 *
 * Team Members: 
 * Akeju Osuolale, 07038243809, olaposiakeju@gmail.com
 * Foluke Olufemi, 09051691752, femioluwole63@yahoo.com
 * Olufemi Olomitutu, 07062311779, faginorish@gmail.com
 * Shuarau Daud, 08028248798, alalani777@gmail.com
 * Ishola Rasheed, 08038340875, ishowtech001@gmail.com
 * Kabir Salam, 07069495725, salamkabirdolapo@gmail.com

 */
package areaofshapes;

import java.util.Scanner;

/**
 *
 * @author CodeLagos Onikan Center
 */
public class AreaOfShapes {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        int menu;
        
        // Declare the Scanner class
        Scanner input = new Scanner(System.in);
        
        System.out.println("1. Circle \n2. Square \n3. Triangle ");
        System.out.print("Please select 1, 2 or 3: \n");
        
        menu = input.nextInt();
        switch(menu) {
            case 1:
                float radius;
                System.out.println("You selected a Circle");
                System.out.print("Please enter a radius for your Circle: \n");
                radius = input.nextFloat();
                float result = (22  * radius * radius) / 7;
                System.out.println("The area of your circle with radius " + radius + " is " + result);
            break;
            case 2:
                int length;
                System.out.println("Please enter the length of your Square:");
                length = input.nextInt();
                int second_result = length * length;
                System.out.println("The area of your Square with length of " + length + " is " + second_result);
            break;
            case 3:
                int rect_length;
                int rect_breadth;
                System.out.println("Please enter the length of your Rectangle:");
                rect_length = input.nextInt();
                System.out.println("Please enter the breadth of your Rectangle:");
                rect_breadth = input.nextInt();
                int third_result = rect_length * rect_breadth;
                System.out.println("The area of your Rectangle with length of " + rect_length + " and breadth of " + rect_breadth + " is " + third_result);
            break;
            default:
                System.out.println("You have made an invalid selection.");
        }
    }
    
}
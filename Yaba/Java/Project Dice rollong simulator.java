//  	Taiwo Abayomi , 
//	Olatunde Demilade , 
// 	Sanusi Shina 
//	Durosinmi Yusuf
//	Ekene Nzekwe 

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package dice.rolling.simulator;
import java.util.*;
import jdk.nashorn.internal.runtime.regexp.joni.Option;

/**
 *
 * @author User
 */
public class DiceRollingSimulator {

    /**
     * @param args the command line arguments
     */ 
    
    
    public static void game(){
        Scanner test = new Scanner(System.in);
        System.out.println("PLAYER 1 Name:");
        String player1Name = test.nextLine();
        System.out.println("PLAYER 2 Name");
        String player2Name = test.nextLine();
        Random rand = new Random();
       int player1score = rand.nextInt(6)+1;
        System.out.println(player1score);
       int player2score = rand.nextInt(6)+1;
        System.out.println(player2score);
        if(player1score > player2score){
            System.out.println(player1Name + "WIN");
            
        
            }else if (player1score < player2score){
            System.out.println(player2Name + "WIN");
            
    
}else{
            System.out.println("draw");         
            }
    }
            
    public static void main(String[] args) {
        // TODO code application logic here
        String option;
        do{
        game();
        Scanner diamon = new Scanner(System.in);
            System.out.println("Enter y to continue and x to exit");
           option  = diamon.nextLine();
        }while(option.equals("Y") || option.equals("y") );
        
    }
}

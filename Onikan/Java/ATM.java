/*
 * Project Name: An Automated Teller Machine (ATM) simulation program
 *
 * Team Members: 
 * Akeju Osuolale, 07038243809, olaposiakeju@gmail.com
 * Foluke Olufemi, 09051691752, femioluwole63@yahoo.com
 * Olufemi Olomitutu, 07062311779, faginorish@gmail.com
 * Shuarau Daud, 08028248798, alalani777@gmail.com
 * Ishola Rasheed, 08038340875, ishowtech001@gmail.com
 * Kabir Salam, 07069495725, salamkabirdolapo@gmail.com

 */
package atm;
import java.util.Scanner;

/**
 *
 * @author CodeLagos Onikan Center
 */

public class ATM{
	public static void main(String []args) {
		//Instantiate our Scanner
		Scanner bank = new Scanner(System.in);
		System.out.println("Please Insert Your Card\n-----------------------");
		
		//Creates pin
		int  option, defaultpin=1234, amount, acctnum, userpin;
		double balance=804.67;
	  String acctype1 = "Savings", acctype2= "Current";
	  
	  //check user's pin
		System.out.println("Enter your pin");
		userpin =bank.nextInt();
		if (userpin == defaultpin) {
			
			//if the PIN is correct
			System.out.println("Please select your transaction type:\n1. Cash Withdrawal \n2. Cash Transfer \n3. Check account balance \n4. Pay bills \n5. Buy recharge card ");
			option =bank.nextInt();
			switch(option) {
			case 1:
				System.out.println("Please enter the amount to withdraw");
				amount=bank.nextInt();
				//int a=1000, b=2000, c=5000, d=10000, e=15000, f=20000, g="other";
				if (amount > balance) {
					System.out.println("Insufficient Balance");
				}
				else
				{
					System.out.println(amount);
				}
			case 2:
				System.out.println("Please enter the acount number you wish to transfer to");
				acctnum=bank.nextInt();
				System.out.println("Enter the amount");
				amount=bank.nextInt();
				if (amount > balance) {
					System.out.println("Insufficient Balance");
				}
				else {
					System.out.println("You're transferring " + amount + " to " + acctnum);
				}
			case 3:{
				System.out.println("Your account balance is " + balance);
			}
			case 4:
				System.out.println("Please select the bill type: \n1. PHCN Bills\n2. DSTV Cable Bill\n3. GOTV\n4. StarTimes\n5. Air Tickets");
		}
			
			}
		else {
			
			//seize the card
			System.out.println("Your card has been seized.");
		}
		
	
	
	
	}
	}
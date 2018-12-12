/*
 * This is the Project for CODELAGOS
 * This is a Console App
 * Name of App: FOODBUK
*  This is a community of People that loves Foods either they want to learn or want to teach someone
 */


import java.util.Scanner;
import javax.swing.JOptionPane;

public class Foodbuk {
    
    public void Intro(){
        System.out.println("This is the Demo Version");
        System.out.println("******** Welcome to FOODBUK ********");
        System.out.println("This is a community of individuals that want cooks, want to learn how to cook\n\t\tand meet chefs from all over the world ");
        
    }
    public void Options(){
        Scanner input = new Scanner(System.in);
        System.out.print("Please Selct input your country: ");
        String country = input.nextLine();
   
        int selection;
        System.out.println("Which category are?\n1.Chef\n2.Novice");
        System.out.print("Selection: ");
        
        selection = input.nextInt();
        if (selection == 1) {
            System.out.println("This option is unavaliable for this version of this App");   
        }if (selection == 2 ) {
            System.out.println("******* Welcome to the Novice Section ********");
            System.out.println("Please we will need some information about you and your Interests");
            System.out.print("Input your First name: ");
            String FN = input.next();
            
            System.out.print("Input your Last name: ");
            String LN = input.next();
            System.out.print("Input your Email Address: ");
           String EM = input.next();
           
            System.out.println("Loading *******");
             System.out.println("Congratulation, You have been registered\n");
        
                   System.out.println("Select the Food that you want to Learn");
                   System.out.println("1.How to cook Jollof Rice\n2.How to cook Egusi Soup\n3.How to make Amala");
  
                  int choice;
                  System.out.println("Selection: ");
                  choice = input.nextInt();
                   if (choice == 1 ){  
                           System.out.println("Ingredients\n" +
"•3¾ cups (750g) long grain parboiled rice\n" +
"•2-3 cups Tomato Stew\n" +
"•Chicken (whole chicken, drumsticks or chicken breast)\n" +
"•Pepper and salt (to taste)\n" +
"•2 medium onions\n" +
"•3 Knorr cubes\n" +
"•2 teaspoons thyme\n" +
"•2 teaspoons curry powder (Nigerian curry powder)"
                                   + "Before you cook Jollof Rice\n" +
"1.Prepare the tomato stew.  It is advisable to prepare tomato stew before hand and keep in the freezer. This is so that whenever you want to cook any jollof rice related dish, it is just a matter of adding it to your cooking.\n" +
"2.If you will use whole chicken then wash and cut it into pieces. Cook with the thyme, Knorr cubes and 2 bulbs of onions (chopped). The cooking time depends on the type of chicken. The rooster or cockerel cooks much faster than the hen but the hen is definitely tastier. When done, grill it in an oven. You may also fry it. This is to give it a golden look which is more presentable especially if you have guests for dinner.\n" +
"3.Parboil the rice using the method detailed in parboiling rice for cooking jollof rice. Rinse the parboiled rice and put in a sieve to drain.\n" +
"\n" +
"Cooking Directions\n" +
"1.Pour the chicken stock and the tomato stew into a sizeable pot and leave to boil.\n" +
"2.Add the drained parboiled rice, curry powder, salt and pepper to taste. The water level should be the same level of the rice. This is to ensure that all the water dries up by the time the rice is cooked.\n" +
"3.Cover the pot and leave to cook on low to medium heat. This way the rice does not burn before the water dries up.\n" +
"\n" +
"If you parboiled the rice as described at parboiling rice for cooking jollof rice, the rice should be done by the time the water is dry. Taste to confirm. If not, you will need to add more water and reduce the heat to prevent burning. Keep cooking till done. \n" +
"\n" +
"Serve with Peppered Fish, Fried Plantains, Nigerian Moi Moi, Nigerian Salad or Coleslaw.\n" +
"\n" +
"You can spice up this recipe by adding 2 well known vegetables to arrive at what we refer to as Mixed Vegetables Jollof Rice.");
                   }
                      if ( choice == 2){
                           System.out.println("Ingredients\n" +
"•4½ cups (600g) Egusi (Melon) seeds\n" +
"•2 cooking spoons red palm oil\n" +
"•Beef: Best cut and Shaki (cow tripe)\n" +
"•Fish: Dry Fish and Stock Fish\n" +
"•3 tablespoons ground crayfish\n" +
"•Pepper and Salt (to taste)\n" +
"•Vegetable: Nigerian pumpkin leaves, spinach or bitter leaves\n" +
"•3 small stock cubes\n" +
"•1 Ogiri Okpei (traditional locust bean seasoning: optional)"
                                   + "Before you cook Egusi Soup (Caking Method)\n" +
"1.Before preparing the soup, soak the dry fish for about half an hour. If you are using the very tough stockfish, boil it for 20 minutes and leave in the pot with the hot water to soak for about an hour. If using the softer stockfish, you can just soak them in cool water till you can break them apart with your hands.\n" +
"2.When the fish and stockfish are soft, debone and break them into sizeable chunks.\n" +
"3.Much closer to your cooking time, grind the egusi with a dry mill. Grind the crayfish and the dry pepper separately and set aside. Wash the vegetable to be used. Cut into tiny pieces.\n" +
"4.Boil the shaki, stock fish and dry fish in 1 litre of water with the stock cubes till they are well done. First sign of a done shaki is that the cuts will start curling on itself.\n" +
"5.Wash the beef to be used for the soup, add it to the pot and cook on medium heat till done.");
}        
                  if (choice == 3 ){
                      System.out.println("INGREDIENTS\n" +
"Water – 1L\n" +
"Yam flour – 2 cups\n" +
"Boiling pot\n" +
"Wooden stick"
                              + "How to make Amala\n" +
"\n" +
"Even if you are not an experienced cook, you can definitely succeed in making Amala in your kitchen. Follow these steps for flavorful, smooth, and lump-free Amala.\n" +
"1.Pour the clean water into the pot and bring it up to a boil on medium heat.\n" +
"2.Once the water starts boiling, turn off the gas. Start gradually adding yam flour. Make sure not to pour in the yam flour while the mixture is still boiling – that way you’ll avoid lumps.\n" +
"3.Mix the flour and water together with a wooden stick. Run the stick through the mixture several times to ensure that it’s smooth and free of any lumps.\n" +
"4.Return the pot to the stove and cook Amala on low heat for up to 5 minutes.\n" +
"5.A good way of telling whether Amala is ready is to use your finger: if the mixture is firm, take it off the heat; if it’s too hard, add some hot water; and if it’s too runny, pour in some more yam flour.\n" +
"6.Wrap the Amala in cling film, plastic bag, or nylon to keep it fresh longer.");
                  } 
        }
         else {
                 System.out.println("Wrong Input");
                 }                
    }
   

    public static void main(String[] args){
     new FoodBook().Intro();
     new FoodBook().Options();
    
    }
    
}

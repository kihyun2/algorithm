import java.util.Scanner;


public class Main {

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();
        int[] alphabet = new int[91];
        word = word.toUpperCase();
        String result = ".";

//        String word = "AB";
//        System.out.println((int)word.charAt(0));
        for(int i = 0; i < word.length(); i++){
            alphabet[(int) word.charAt(i)]++;
        }
        int tmp = 0;
        for(int i = 0; i < alphabet.length; i++){
            if (tmp < alphabet[i]){
                tmp = alphabet[i];
                result = (char)i+"";
            } else if (tmp == alphabet[i]) {
                result = "?";
            }
        }
        System.out.println(result);

    }
}
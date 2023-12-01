import java.util.Arrays;
import java.util.Scanner;


public class Main {

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
//        int[] N = new int[9];
        int a;
        int result = -1;
        int idxpo = 0;
        for(int i = 1; i<9+1; i++){
//            N[i] = sc.nextInt();
            a = sc.nextInt();
            if(result < a){
                result = a;
                idxpo = i;
            }
        }
        System.out.println(result);
        System.out.println(idxpo);
    }
}
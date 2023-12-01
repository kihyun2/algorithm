import java.util.Scanner;


public class Main {

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int tmp = 1;
        int[] num = new int[10];
        for(int i = 0; i < 3; i++){
            tmp *= sc.nextInt();
        }
        String str = tmp+"";
        for (int i = 0; i < str.length(); i++) {
            int idx = Integer.parseInt(str.toCharArray()[i]+"");
            num[idx]++;
        }
        for (int i = 0; i < 10; i++) {
            System.out.println(num[i]);
        }
    }
}
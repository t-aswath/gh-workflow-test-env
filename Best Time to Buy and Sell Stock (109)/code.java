import java.util.*;

class Solution {
    public boolean canAchieveDivisibleProfit(int[] prices, int k) {
        int min_price = Integer.MAX_VALUE;
        int max_profit = 0;
        
        for (int price : prices) {
            min_price = Math.min(min_price, price);
            max_profit = Math.max(max_profit, price - min_price);
        }
        
        return max_profit > 0 ? (max_profit % k == 0) : false;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        
        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt();
            int[] prices = new int[n];
            
            for (int j = 0; j < n; j++) {
                prices[j] = scanner.nextInt();
            }
            
            int k = scanner.nextInt();
            Solution solution = new Solution();
            if (solution.canAchieveDivisibleProfit(prices, k)) {
                System.out.println("True");
            } else {
                System.out.println("False");
            }
        }
        
        scanner.close();
    }
}

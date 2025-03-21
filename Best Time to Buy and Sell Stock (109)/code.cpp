#include <iostream>
#include <vector>
#include <limits>
using namespace std;

class Solution {
public:
    bool canAchieveDivisibleProfit(vector<int>& prices, int k) {
        int min_price = numeric_limits<int>::max();
        int max_profit = 0;
        
        for (int price : prices) {
            min_price = min(min_price, price);
            max_profit = max(max_profit, price - min_price);
        }
        
        return (max_profit > 0) ? (max_profit % k == 0) : false;
    }
};

int main() {
    int t;
    cin >> t;
    
    for (int i = 0; i < t; ++i) {
        int n;
        cin >> n;
        
        vector<int> prices(n);
        for (int j = 0; j < n; ++j) {
            cin >> prices[j];
        }
        
        int k;
        cin >> k;
        
        Solution solution;
        cout << (solution.canAchieveDivisibleProfit(prices, k) ? "True" : "False") << endl;
    }
    
    return 0;
}

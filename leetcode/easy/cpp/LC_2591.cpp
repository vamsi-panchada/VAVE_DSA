#include <iostream>

using namespace std;

class Solution {
public:
    int distMoney(int money, int children) {
        if(money<children) {
            return -1;
        }
        money -= children;
        int children_with_8 = money/7;
        if(children_with_8 > children) {
            children_with_8 = children;
        }
        money -= (children_with_8*7);
        int children_with_1 = children-children_with_8;
        if((children_with_1 == 0 && money > 0) || (children_with_1 == 1 && money == 3)) {
            return children_with_8 - 1;
        }
        return children_with_8;
    }
};

int main() {
    Solution solution;
    int money, children;
    cin >> money;
    cin >> children;
    cout << solution.distMoney(money=money, children=children);
    return 0;
}
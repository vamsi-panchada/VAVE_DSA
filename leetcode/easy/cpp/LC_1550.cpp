#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        int n = arr.size();
        for(int i = 0; i < n - 2; ++i) {
            if((arr[i] % 2 != 0) && (arr[i + 1] % 2 != 0) && (arr[i + 2] % 2 != 0)) {
                return true;
            }
        }
        return false;
    }
};

int main() {
    Solution solution;
    vector<int> arr;
    int input;

    while (cin >> input) {
        arr.push_back(input);
    }

    if (solution.threeConsecutiveOdds(arr)) {
        cout << "true";
    } else {
        cout << "false";
    }
    return 0;
}
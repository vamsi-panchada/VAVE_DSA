#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    bool equalFrequency(string word) {
        unordered_map<char, int> counter;
        for(char i: word) {
            counter[i]++;
        }
        vector<int> frequencies;

        for(auto& p: counter) {
            frequencies.push_back(p.second);
        }

        for(int i=0; i<frequencies.size(); i++) {
            frequencies[i]--;
            
            unordered_set<int> freqSet;
            for(int freq: frequencies) {
                if(freq > 0) {
                    freqSet.insert(freq);
                }
            }

            if(freqSet.size() == 1) {
                return true;
            }

            frequencies[i]++;
        }

        return false;

    }
};

int main() {
    Solution solution;
    string word;
    cin >> word;
    cout << (solution.equalFrequency(word) ? "true" : "false") << endl;
    return 0;
}
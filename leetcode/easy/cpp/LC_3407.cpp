#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool hasMatch(string s, string p) {
        int n = s.length();

        size_t pos = p.find('*');
        string prefix = p.substr(0, pos);
        string sufix = p.substr(pos+1);

        int prefix_len = prefix.length();
        int sufix_len = sufix.length();

        bool prefix_found = (prefix_len == 0);
        bool sufix_found = (sufix_len == 0);

        int idx = 0;

        while(!prefix_found && idx <= n-prefix_len) {
            if(s.substr(idx, prefix_len) == prefix) {
                prefix_found = true;
                idx += prefix_len;
            } else {
                idx++;
            }
        }

        while(prefix_found && idx <= n-sufix_len) {
            if(s.substr(idx, sufix_len) == sufix) {
                sufix_found = true;
                break;
            }
            idx++;
        }
        return prefix_found && sufix_found;
    }
};

int main() {
    Solution solution;
    string s, p;
    cin >> s;
    cin >> p;
    cout << (solution.hasMatch(s=s, p=p)? "true": "false");
    return 0;
}
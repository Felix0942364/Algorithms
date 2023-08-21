#include <string>
#include <vector>
#include <unordered_map>
#include <set>

using namespace std;

vector<int> solution(vector<string> gems) {
    vector<int> answer(2);
    set<string> kinds;
    for (int i = 0; i < gems.size(); i++)
        kinds.insert(gems[i]);
    
    int minLen = 100000;
    unordered_map<string, int> count;
    int i;
    int start = 0;
    int end = 0;
    
    while (true) {
        for(i = end; i < gems.size(); i++) {
            count[gems[i]]++;
            if (count.size() == kinds.size()) {
                end = i;
                break;
            }
        }
        
        if (i == gems.size())
            break;
        
        for (i = start; i < gems.size(); i++) {
            if (count[gems[i]] == 1) {
                start = i;
                break;
            }
            else
                count[gems[i]]--;
        }
        
        if (end - start < minLen) {
            answer[0] = start+1;
            answer[1] = end+1;
            minLen = end - start;
        }
        
        count.erase(gems[i]);
        start++;
        end++;
    }
    
    return answer;
}
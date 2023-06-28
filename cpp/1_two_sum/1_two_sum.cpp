#include<vector>
#include<unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;
        int i = 0;
        do {
            if (mp.count(target - nums[i])){
                return {mp[target - nums[i]], i};
            }
            mp[nums[i]] = i;
            ++i;
        } while(i < nums.size());
        return {};
    }
};

int main() {
    return 0;
}
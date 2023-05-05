#include <iostream>
#include <vector>
#include <algorithm>
#include <set>

int main() {
    int n, k;
    std::cin >> n >> k;
    std::vector<std::pair<int, int>> times;
    for (int i = 0; i < n; i++){
        std::pair<int, int> p;
        std::cin >> p.first >> p.second;
        times.push_back(p);
    }
    sort(times.begin(), times.end(), [](std::pair<int, int> a, std::pair<int, int> b) {
        if (a.second != b.second)
        return a.second < b.second;
        return a.first > b.first;
    });

    int count = 0;
    std::multiset<int> m;
    std::multiset<int>::iterator iter;
    for (int i = 0; i < k; i++) m.insert(0);
    for (int i = 0; i < n; i++) {
        iter = m.upper_bound(times[i].first);
        if (iter != m.begin()) {
            m.erase(--iter);
            m.insert(times[i].second);
            count++;
        }
    }
    std::cout << count << std::endl;
    return 0;
}
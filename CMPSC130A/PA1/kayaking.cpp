#include <iostream>
#include <vector>
#include <algorithm>

int person[3], strength[3], speed[50000]; 
int kayaks;


bool canMakeSpeed(int speed) {
    /*
    int p[3];
    std::copy(person, person+3, p);
    int lowestPersonIndex = 1, highestPersonIndex = kayaks*2;
    
    for (int i = 0; i < kayaks; i++){
        int lowest = getLowest(p);
        int highest = getHighest(p);
        p[lowest]--;
        int secondLowest = getLowest(p);
        
        if (speeds[i] * (strength[lowest] + strength[secondLowest]) >= speed) {
            p[secondLowest]--;
            continue;
        }
        if (speeds[i] * (strength[lowest] + strength[highest] < speed)) return false;
        if (lowest == 0 && highest == 2 && p[1] != 0 && speeds[i] * (strength[lowest] + strength[1]) >= speed) {
            p[1]--;
            continue;
        }
        p[highest]--;
    }*/
    return true;
}

int main() {
    std::cin >> person[0] >> person[1] >> person[2];
    std::cin >> strength[0], strength[1], strength[2];
    kayaks = (person[0] + person[1] + person[2])/2;
    
    for (int i = 0; i < kayaks; i++) {
        std::cin >> speed[i];
    }
    std::sort(speed, speed + kayaks);
    
    int left = 1, right = 2000 * 100000, ans = 0;
    while(left <= right) {
        int mid = (left + right) / 2;
        if (canMakeSpeed(mid)){
            ans = std::max(ans, mid);
            left = mid + 1;
        }
        else right = mid-1;
    }
    std::cout << ans;
    return 0;
}
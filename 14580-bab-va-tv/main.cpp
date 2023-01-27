#include <iostream>

using namespace std;

int main() {
    int n, k, x;
    cin >> n >> k;
    cin >> x;
    string names[n];
    for (int i = 0; i < n; ++i) {
        cin >> names[i];
    }

    int c = (x + k);
    if(c > n) c--;
    c = c % n;
    cout << names[c];
    return 0;
}
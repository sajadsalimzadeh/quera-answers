
#include <iostream>
using namespace std;

int main()
{
    int n;
    int sum = 0;
    int count = 0;

    cin >> n;

    for (int i = 1; i <= n; i++) {

        for (int j=1;j<=i;j++){
            if (i%j==0) {
                sum+= j;
                count++;
            }

        }

    }

    cout << count << " " << sum;


    return 0;
}
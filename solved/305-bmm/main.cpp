#include <iostream>
using namespace std;

int bmm(long long int n1, long long int n2)
{
    if (n2 != 0)
        return bmm(n2, n1 % n2);
    else
        return n1;
}

int main()
{
    long long int n1, n2;

    cin >> n1;
    cin >> n2;

    cout << bmm(n1, n2);

    return 0;
}

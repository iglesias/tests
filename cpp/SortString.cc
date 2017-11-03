#include <algorithm>
#include <string>
#include <iostream>

#define ALL(a)  (a).begin(), (a).end()

using namespace std;

bool f(string& str1, string& str2)
{
    if (str1.length() != str2.length())
        return false;

    sort(ALL(str1));
    sort(ALL(str2));

    return str1==str2;
}

int main()
{
    string str1, str2;

    cout << "Enter the first string: ";
    cin >> str1;

    cout << "Enter the second string: ";
    cin >> str2;

    if (f(str1, str2))
        cout << "They are palindromes" << endl;
    else
        cout << "They are not palindromes" << endl;

    return 0;
}

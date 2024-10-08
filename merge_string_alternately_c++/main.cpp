#include <iostream>
#include "solution.cpp"

#include <string>
using namespace std;

int main()
{
    cout << "start" << '\n';

    Solution sol;
    string result;
    result = sol.mergeAlternately("abc","defgh");
    cout << result << '\n';

    cout << "end" << '\n';
}

//
//  알고리즘.cpp
//  treee
//
//  Created by Apple on 2020/03/25.
//  Copyright © 2020 minjae. All rights reserved.
//
#include <iostream>
#include <string>
using namespace std;

bool check(string s) {
    int arr[26] = {0};
    if(s.length() == 1)
        return true;
    for(int i=0; i<s.length(); i++) {
        if(arr[s[i] - 'a'] == 1)
             return false;
        if(s[i] == s[i+1]) {
            arr[s[i] - 'a'] = 0;
            
        }
        else {
            arr[s[i] - 'a'] = 1;
          
        }
    }
    return true;
}
int main()
{
    int n;
    int count = 0;
    string s;
    cin>>n;
    for(int i=0; i<n; i++) {
        cin>>s;
        if(check(s))
            count++;
    }
    
    cout<<count;
    
}



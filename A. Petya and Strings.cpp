#include<bits/stdc++.h>
using namespace std;

int main(){
string s1, s2;
int c;
cin>>s1;
cin>>s2;
transform(s1.begin(), s1.end(), s1.begin(), ::tolower);
transform(s2.begin(), s2.end(), s2.begin(), ::tolower);

if(s1>s2)
    c=1;
else if(s1==s2)
    c=0;
else
    c=-1;
cout<<c;


  return 0;
}

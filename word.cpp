#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;

int main (){
 string s;
 int upper=0, lower=0;

cin>>s;
for(int i=0; i<s.size(); i++ ){
    if(s[i]>=97 && s[i]<=122){
        lower++;
    }
     else if  (s[i]>=65 && s[i]<=90)
          upper++;
}
if (lower> upper){
        transform(s.begin(), s.end(), s.begin(), ::tolower);

  		cout<<s; }

  	else if (upper>lower){
        transform(s.begin(), s.end(), s.begin(), ::toupper);

  		cout<<s;
  	}

  	else{
     transform(s.begin(), s.end(), s.begin(), ::tolower);

  		cout<<s;
}





return 0;
}

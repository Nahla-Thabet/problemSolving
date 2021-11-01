#include<iostream>
#include<stack>
using namespace std;

int main(){
int n;
int arr[n];
int Count =1 ;
cin>>n;

for (int i =0; i<n ; i++){
    cin>>arr[i];
}
for (int i =0; i<n-1 ; i++){
    if (arr[i] != arr[i+1]){
        Count++;
    }
}
cout<< Count;
return 0;
}

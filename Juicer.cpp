#include <iostream>
#include <cstring>
#include <string>
using namespace std;

int main ()
{
	int s1,s2,s3;
	cin>>s1>>s2>>s3;
	int sum=0;
	int waste=0;
	int arr[s1];
	for(int i=0; i<s1;i++)
	{
		cin>>arr[i];
		if (arr[i]<=s2)
		{
			waste+=arr[i];
			if (waste > s3)
			{
				sum++;
				waste=0;
			}
		}
	}
	cout <<sum;

}

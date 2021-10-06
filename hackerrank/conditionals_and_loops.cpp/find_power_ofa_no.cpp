// Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to print the answer.

#include<iostream>
using namespace std;

int main(){

   
    int x,n,i;
   int ans=1;
    cin>>x>>n;
    for(i=1;i<=n;i++){
        ans = ans*x;

    }
    cout<<ans;

  return 0;
}
// Write a program to input an integer N and print the sum of all its even digits and sum of all its odd digits separately.
// Digits mean numbers, not the places! That is, if the given integer is "13245", even digits are 2 & 4 and odd digits are 1, 3 & 5.
// Input format :

#include<iostream>
using namespace std;


int main(){

   int n;
   cin>>n;
   int odd=0;
   int even=0;
   int div;
   
   
   while(n>0){
           div=n%10;
           n=n/10;
           if(div%2==0){
               even=even+div;
           }
           else{
               odd=odd+div;
           }
      

   }
   cout<<even<<" "<<odd;
}
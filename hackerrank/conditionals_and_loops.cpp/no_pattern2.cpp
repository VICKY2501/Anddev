// Number Pattern 2
// Send Feedback
// Print the following pattern
// Pattern for N = 4
// ...1
// ..23
// .345
// 4567

// The dots represent spaces.

#include<iostream>
using namespace std;


int main(){

   int n;
   cin>>n;
   int i=1;
   
   
   while(i<=n){
       int k=1;
       while(k<=n-i){
       cout<<" ";
       k++;
   }
      int j=1;
      int val=i;
    
          while(j<=i){
              cout<<val;
              val++;
              j++;
          }
          cout<<endl;
          i++;
      
   }
}



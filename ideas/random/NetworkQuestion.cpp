#include <iostream>
#include <random>
using namespace std;
int rando (int num1,int num2) //random function
    {
    random_device rand;  
    mt19937 gen(rand());  
    uniform_int_distribution<>dis(num1, num2);
    return dis(gen);
    }
int main()
{
    //this is another test pablo
     char x='y',s;
     int repeat,g,subnet;
     while(true)
     {
    sdsd:
    g=rando(1,3);
    if(g==repeat){goto sdsd;}
    else
    {
    s=(g==1) ? 'A' : (g==2) ? 'B':'C';
    subnet=(g==1)? rando(8,32):(g==2)?rando(16,32):rando(24,32);
    cout<<rando(1,255)<<"."<<rando(20,200)<<"."<<rando(10,140)<<"."<<rando(1,255)<<"/"<<subnet<<endl;
    cout<<"Class: "<<s<<endl;
    if(g<=2){cout<<true;}
    cin>>x;
    }
    // test
    //test
    repeat=g;
    }
}
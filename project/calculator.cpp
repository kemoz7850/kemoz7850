#include <iostream>
#include <vector>
using namespace std;
int main()
{
    vector<string> brac;
    vector<int> filter,index,checked[3];
    int count = 0;
    string eq;
    cin>>eq;
    for(int i = 0; i < eq.length() ; i++)
    {
        if(eq[i] == '(')
        {
            brac.push_back("o"+ to_string(++count));
            index.push_back(i);
        }
        if(eq[i] == ')')
        {
            brac.push_back('b'+ to_string(count--));
            index.push_back(i);
        }
    }

for(int i = 0; i < brac.size() ; i++)
{
   if(brac[i][0] == 'o') 
   {
        for(int j = 0 ; j < brac.size() ; j++)
        {
        int counter = 0;
            for(int z = 0 ; z < filter.size() ; z++)
            {
                if(index[i] != filter[z] && index[j]!=filter[z])
                {
                    counter++;
                }
            }
            if(brac[i][1] == brac[j][1] && brac[j][0] == 'b' && counter == filter.size())
            {
                checked[0].push_back(index[i]);
                checked[1].push_back(index[j]);
                filter.push_back(index[i]);
                filter.push_back(index[j]);
            }
        }
   }
}
for(int i = 0 ; i < checked[0].size() ; i++)
    {
        int count=0;
        for(int j = 0 ; j < checked[0].size() ; j++)
        {
            if(checked[0][j] > checked[0][i] && checked[1][j] < checked[1][i])
            {
                count++;
            }
        }
        checked[2].push_back(count);
    }
    for(int i = 0 ; i < checked[0].size() ; i++)
    {
        for(int j = 0 ; j < checked[0].size(); j++)
        {
            if(checked[2][i] < checked[2][j])
            {
                int temp[3]{checked[0][i],checked[1][i],checked[2][i]};
                checked[0][i] = checked[0][j];
                checked[1][i] = checked[1][j];
                checked[2][i] = checked[2][j];
                checked[0][j] = temp[0];
                checked[1][j] = temp[1];
                checked[2][j] = temp[2];
            }
        }
    }
    for(int i = 0 ; i < checked[0].size() ; i++)
    {
        cout<<checked[0][i]<<"----"<<checked[1][i]<<"----"<<checked[2][i]<<endl;
    }
}
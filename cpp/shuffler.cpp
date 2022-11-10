#include "shuffler.h"
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

string hello()
{
    return "hellow world";
}

//generates all possible combinations of the *numbers* parameter with a *lenght* length (more info below)
//source : https://www.tutorialspoint.com/cplusplus-program-to-generate-all-possible-combinations-out-of-a-b-c-d-e
void Combi(int* numbers, int reqLen, int currIdx, int currLen, bool* check, int length, vector<vector<int>> &allCombi)
{
   if(currLen > reqLen)
   return;
   else if (currLen == reqLen) {
      vector<int> currentCombi;
      for (int i = 0; i < length; i++) {
         if (check[i] == true) {
            currentCombi.push_back(numbers[i]);
         }
      }
      allCombi.push_back(currentCombi);
      return;
   }
   if (currIdx == length) {
      return;
   }
   check[currIdx] = true;
   Combi(numbers, reqLen, currIdx + 1, currLen + 1, check, length,allCombi);
   check[currIdx] = false;
   Combi(numbers, reqLen, currIdx + 1, currLen, check, length,allCombi);
}

//generates the permutations possible between 0 and nbElements-1 of the reqLen length
vector<vector<int>> generate_perm(const int  nbElements,const int reqLen)
{
    vector<int> indexes;
    for (int i=0; i<nbElements;i++)
    {
        indexes.push_back(i);
    }
    bool* check=new bool[nbElements]{};
    vector<vector<int>> allCombi;
    Combi(&indexes[0],reqLen,0,0,check,nbElements,allCombi);
    delete[] check;
    vector<vector<int>> res;
    for(vector<int> vect:allCombi)
    {
        res.push_back(vect);
        while(next_permutation(&vect.front(),&vect.front()+reqLen))
        {
            res.push_back(vect);
        }
    }
    cout<<"perm generated "<<res.size()<<endl;
    return res;
}

//generate all string pairs possible with tab1 elements in 1st position and tab2 elements in 2nd position
vector<string> generate_pairs(vector<string> tab1,vector<string> tab2)
{
    vector<string> res;
    for(string st1 : tab1)
    {
        for (string st2 : tab2)
        {
            if(!(st1+st2).empty())
            res.push_back(st1+st2);
        }
    }
    return res;
}

vector<vector<string>> shuffle(vector<vector<string>> input,int size)
{
    if (input.size()==0 || size==0)
    {
        return {};
    }
    vector<vector<string>> res;
    vector<vector<int>> permutations = generate_perm(input.size(),size);
    for (vector<int> perm:permutations)
    {
        vector<string> seed=input[perm[0]];
        for (int i=1;i<perm.size();i++)
        {
            seed=generate_pairs(seed,input[perm[i]]);
        }
        if(seed.size()>0)
        {
            res.push_back(seed);
        }
    }
    return res;
}

int main()
{
    vector<string> tab1={"toto","tata","titi"};
    vector<string> tab2={"coco","caca"};
    vector<string> tab3={"lolo"};
    vector<string> tab4={};
    vector<vector<string>> input = {tab1,tab2,tab3,tab4};
    vector<vector<string>> out=shuffle(input,3);
    for (vector<string> vect:out)
    {
        for(string str:vect)
        {
            cout<<str<<" ";
        }
        cout<<endl;
    }
}


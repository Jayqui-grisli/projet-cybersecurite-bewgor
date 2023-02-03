#include "shuffler.h"
#include <iostream>
#include <algorithm>
#include <vector>
#include <chrono>

using namespace std;

string hello()
{
    return "hellow world";
}

void mixedUpperBis(string &word,bool* check,int currIdx, vector<string> &out_dico)
{
    if (currIdx>word.length())
    {
        return;
    }
    else if (currIdx==word.length())
    {
        string tempword="";
        for (int i=0;i<word.length();i++)
        {
            if (check[i])
            {
                tempword+=toupper(word[i]);
            }
            else
            {
                tempword+=word[i];
            }
        }
        out_dico.push_back(tempword);
        return;
    }
    check[currIdx]=true;
    mixedUpperBis(word,check,currIdx+1,out_dico);
    check[currIdx]=false;
    mixedUpperBis(word,check,currIdx+1,out_dico);
    return;
}

vector<string> mixedUpper(string word)
{
    bool* check=new bool[word.length()]{};
    vector<string> out_dico;
    mixedUpperBis(word,check,0,out_dico);
    delete[] check;
    return out_dico;
}

void shuffleBis(vector<string>&input,int size,int* indexes,int currentCount,string cache,vector<string> &outdico)
{
    if (currentCount>size)
    {
        return;
    }
    else if (currentCount<size)
    {
        for (int i=0;i<input.size();i++)
        {   
            if (!isInArray(indexes,i,currentCount))
            {
                indexes[currentCount]=i;
                shuffleBis(input,size,indexes,currentCount+1,cache+input[i],outdico);
            }
        }
    }
    else if(currentCount==size)
    {   
        outdico.push_back(cache);
    }
}

vector<string> shuffle(vector<string> input, int size)
{
    if(size<=1)
    {
        return input;
    }
    else
    {
        int* indexes=new int[size];
        vector<string> out_dico;
        shuffleBis(input,size,indexes,0,"",out_dico);
        delete[] indexes;
        return out_dico;
    }
}

bool isInArray(int* array,int item,int size)
{
    for (int i =0;i<size;i++)
    {
        if (array[i]==item)
        {
            return true;
        }
    }
    return false;
}


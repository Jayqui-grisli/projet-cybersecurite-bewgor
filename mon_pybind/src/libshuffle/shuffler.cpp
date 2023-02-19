#include "shuffler.h"
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <chrono>
#include <mutex>

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


void shuffleBis(vector<string>&input,int size,int currentCount,string &cache,vector<string> &outdico,bool firstRound,vector<string>::iterator iter,int start,int finish)
{
    if (currentCount>size)
    {
        return;
    }
    else if (currentCount<size && firstRound)
    {
        for (int i=start;i<finish;i++)
        {   
            string tmp=cache+*(iter+i);
            shuffleBis(input,size,currentCount+1,tmp,outdico,false,iter,start,finish);
        }
    }
    else if (currentCount<size && !firstRound)
    {
        for (int i=0;i<input.size();i++)
        {   
            string tmp=cache+input[i];
            shuffleBis(input,size,currentCount+1,tmp,outdico,false,iter,start,finish);
        }
    }
    else if(currentCount==size)
    {   
        outdico.push_back(cache);
    }
}

void worker(vector<string> &input,int size,vector<string>::iterator iter,int start,int finish,ofstream &myfile,string &filename, mutex &mtx)
{
    cout<<"thread started"<<endl;
    vector<string> out_dico;
    string cache="";
    shuffleBis(input,size,0,cache,out_dico,true,iter,start,finish);
    lock_guard<mutex> lock(mtx);
    cout<<"thread writing"<<endl;
    myfile.open(filename,ios::app);
    for (auto word : out_dico)
    {
        myfile<<word<<endl;
    }
    myfile.close();
    cout<<"thread finished writing"<<endl;
}

vector<string> shuffle(vector<string> input, int size, string filename)
{
    if(size<=1)
    {
        return input;
    }
    else
    {
        cout<<"main thread started"<<endl;
        int quarter=input.size()/4;
        mutex mtx;
        ofstream myfile;
        myfile.open(filename,ios::trunc);
        myfile.close();
        vector<string>::iterator iter = input.begin();
        thread worker1(worker,ref(input),size,iter,0,quarter,ref(myfile),ref(filename),ref(mtx));
        thread worker2(worker,ref(input),size,iter,quarter,2*quarter,ref(myfile),ref(filename),ref(mtx));
        thread worker3(worker,ref(input),size,iter,2*quarter,3*quarter,ref(myfile),ref(filename),ref(mtx));
        thread worker4(worker,ref(input),size,iter,3*quarter,int(input.size()),ref(myfile),ref(filename),ref(mtx));
        worker1.join();
        worker2.join();
        worker3.join();
        worker4.join();
        cout<<"main thread ended"<<endl;
        vector<string> out_dico={};
        return out_dico;
    }
}





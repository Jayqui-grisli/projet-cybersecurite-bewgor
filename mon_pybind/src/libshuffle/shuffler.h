#ifndef shuffler
#define shuffler
#include <iostream>
#include <vector>

std::string hello();
void Combi(int* numbers, int reqLen, int currIdx, int currLen, bool* check, int length,std::vector<std::vector<int>> &allCombi);
std::vector<std::vector<int>>  generate_perm(const int  nbElements,const int reqLen);
std::vector<std::string> shuffle(std::vector<std::string> input,int size);
void mixedUpperBis(std::string word,bool* check,int currIdx, std::vector<std::string> &out_dico);
std::vector<std::string> mixedUpper(std::string word);




#endif
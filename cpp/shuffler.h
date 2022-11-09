#ifndef shuffler
#define shuffler
#include <iostream>
#include <vector>

std::string hello();
std::vector<std::string> generate_pairs(std::vector<std::string> tab1,std::vector<std::string> tab2);
void display_vector(std::vector<std::string> tab);
void combi(int* numbers, int reqLen, int currIdx, int currLen, bool* check, int length,std::vector<std::vector<int>> &allCombi);
std::vector<std::vector<int>>  generate_perm(const int  nbElements,const int reqLen);
std::vector<std::vector<std::string>> shuffle(std::vector<std::vector<std::string>> input);


#endif
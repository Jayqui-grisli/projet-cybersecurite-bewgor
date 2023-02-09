#ifndef shuffler
#define shuffler
#include <iostream>
#include <vector>

std::string hello();
void mixedUpperBis(std::string &word,bool* check,int currIdx, std::vector<std::string> &out_dico);
std::vector<std::string> mixedUpper(std::string word);

void shuffleBis(std::vector<std::string>&input,int size,int currentCount,std::string &cache,std::vector<std::string> &outdico);
std::vector<std::string> shuffle(std::vector<std::string> input,int size);

#endif
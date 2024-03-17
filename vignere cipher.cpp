#include<iostream>
#include<string>
using namespace std;

string encode(const string& word, const string& key) {
    string result;
    string extended_key = key;

    while (extended_key.length() < word.length()) {
        extended_key += key;
    }
  
    extended_key = extended_key.substr(0, word.length());

    for (int j = 0; j < word.length(); ++j) {
        if (isalpha(word[j])) {
            char C = toupper(word[j]);
            char K = toupper(extended_key[j]);
            char encryptedChar = ((C - 'A') + (K - 'A')) % 26 + 'A';
            result += encryptedChar;
        } else {       
            result += word[j];
        }
    }
    return result;
}

int main() {
    string message, key;
    cout << "Enter your message:";
    getline(cin, message);
    cout << "Enter your key:";
    getline(cin, key); 
    string encrypted_message = encode(message, key);
    cout << "Encrypted message:" << encrypted_message << endl;

    return 0;
}
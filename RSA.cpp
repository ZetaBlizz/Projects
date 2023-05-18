#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cmath> //used for floor
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/lexical_cast.hpp>

/*------------------RSA-Steps---------------------------------------------------
Made with the onlinegbd.com/online_c++_compiler
1. Choose secret primes p and q and compute n = pq.
2. Choose e with gcd(e, (p — l)(q - 1)) = 1.
3. Compute d with d*e = 1 (mod (p - l)(q — 1)).
4. Make n and e public, and keep varibles p, q, d secret.
5. Another person encrypts their message m
as c=m^e (mod n) and sends it to their desired party.
6. Decrypt m by computing c^d (mod n).
------------------------------------------------------------------------------*/

//Modifies vector q for quotients neccessary for extended Euclidean Algo
void getQuotients(long long int a, long long int b, std::vector < long long int > & q) {
  long long int quotient = floor(a / b);
  long long int remainders = a - (quotient * b);
  q.push_back(quotient);
  if (remainders == 0) {
    return;
  }
  getQuotients(b, remainders, q);
}

long long int gcd(long long int a, long long int b) {
  if (b == 0) {
    return a;
  } else {
    return gcd(b, a % b);
  }
}

long long int getX(std::vector < long long int > q, std::vector < long long int > xs) {
  for (int i = 0; i < q.size() - 1; i++)
    xs.push_back(-q[i] * xs[i + 1] + xs[i]);
  return xs[xs.size() - 1];
}

//returns d such that d*e = 1 mod (n)
long long int xeuclideanAlgo(long long int a, long long int b) {
  if (b > a) {
    return xeuclideanAlgo(b, a);
  }
  std::vector < long long int > quotients;
  getQuotients(a, b, quotients);
  std::vector < long long int > xTable {0,1};
  long long int x = getX(quotients, xTable);
  return x;
}

//Calculates c^d mod n to retrive the encrypted message or encrypt.
boost::multiprecision::cpp_int encryptDecrypt(boost::multiprecision::cpp_int a, long long int b, boost::multiprecision::cpp_int n) {
  std::vector < boost::multiprecision::cpp_int > squaredMod {
    a
  };
  std::map < long long int, long long int > exponentTable;
  int index = 1;
  long long int exponent = 2;
  boost::multiprecision::cpp_int result;
  long long int last;

  /*Saves modular exponentiation calculation c^2,c^4,c^8,c^16... 
  until exponent is more than d*/
  while (exponent <= b) {
    result = (squaredMod[index - 1] * squaredMod[index - 1]) % n;
    squaredMod.push_back(result);
    exponentTable[exponent] = index;
    index += 1;
    last = exponent;
    exponent *= 2;
  }

  b -= last;

  boost::multiprecision::cpp_int factor = squaredMod[exponentTable[last]];
  long long int candidate;
  long long int key;

  /*uses previous exponentTable to get a+b+...+z = d and multiplies
  their values in squaredMod*/
  while (b > 1) {
    for (auto const & keys: exponentTable) {
      key = keys.first;
      if (b >= key) {
        candidate = key;
      } else {
        break;
      }
      b -= candidate;
      factor = factor * squaredMod[exponentTable[candidate]] % n;
    }
  }

  if (b == 1) {
    return (factor * a) % n;
  }
  return factor;
}

std::vector < std::string > encryptMessage(std::string a, long long int e, boost::multiprecision::cpp_int n) {
  std::string converted;
  int number;
  
  //Maps A,b,c,...,z to 01,02,03,..., 26 using ASCII values
  for (int i=0; i < a.length(); i++) {
    char keys = a[i];
    number = int(keys);
    if (number < 92) {
      number += 32;
    }
    number -= 96;
    if (number < 10) {
      std::string holder = "0" + std::to_string(number);
      converted += holder;
    } else {
      converted += std::to_string(number);
    }
  }

  std::cout << "Converted to int: " << converted << std::endl;

  std::string modN = boost::lexical_cast < std::string > (n);
  long long int start = 0;
  long long int length = modN.length() - 2;
  long long int blocks = length;
  long long int messageLength = converted.length();
  std::vector < std::string > messages;

  //checks if encrypted message needs to be cut into smaller messages due to modn restraint
  if (messageLength > length) {
    int flag = 0;
    while (messageLength >= start) {
      if (converted[start] == '0') {
        start += 1;
        flag += 1;
      }
      boost::multiprecision::cpp_int cut = boost::lexical_cast < boost::multiprecision::cpp_int > (converted.substr(start, blocks));
      std::string encryptCut = boost::lexical_cast < std::string > (encryptDecrypt(cut, e, n));
      if (flag == 1) {
        encryptCut.insert(0, "0");
        flag -= 1;
      }
      messages.push_back(encryptCut);
      start += blocks;
    }
    return messages;
  } else {
    messages.push_back(boost::lexical_cast < std::string > (converted));
    return messages;
  }
}

std::string convertToLetters(std::string m) {
  std::string decrypted;
  int lengthM = m.length();

  if (lengthM % 2 != 0) {
    decrypted += char(int(m[0] - '0') + 96);
    int i = 1;
    while (i < lengthM) {
      decrypted += char(int(m[i] - '0') * 10 + int(m[i + 1] - '0') + 96);
      i += 2;
    }
    return decrypted;
  } else {
    int i = 0;
    while (i < lengthM) {
      decrypted += char(int(m[i] - '0') * 10 + int(m[i + 1] - '0') + 96);
      i += 2;
    }
    return decrypted;
  }
}

int RSA() {
  /*If you're' using a number bigger than 8 bytes
  make sure to replace long long ints with boosts multiprecision.
  The link below has the first trillion primes listed,
  they can be used for p,q, and e. Make sure to pick randomly.
  http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php*/

  //--------Sample dataset---------------
  long long int p = 885320963;
  long long int q = 238855417;;
  long long int n = p * q;
  long long int e = 9007;
  long long int s = (p - 1) * (q - 1);
  if (gcd(e, s) != 1) {
    std::cout << "e does not satisfy the condition gcd(e, s) = 1, please choose another e to calculate d with" << std::endl;
    return 0;
  }
  long long int d = xeuclideanAlgo(e, s);
  while (d < 0) {
    d += s;
  }

  /*--------------ENCRYPTION--------------------------------------------------
  Future version needs to replace Lexical_cast for
  longer strings than 88 characters and further optimizations can be made
  by checking if a cycle exists in  the modular exponentiation calculator*/
  std::string message = "asmABCDEFGHIJKLMNOPQRSTUVWXYZtestTwoaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz";
  long long int encryptionExponent = e;
  boost::multiprecision::cpp_int modn = n;
  std::vector < std::string > encrypted = encryptMessage(message, encryptionExponent, modn);
  std::cout << "Send these numbers to desired party (along with n: " << n << " and e: " << e <<"):" << std::endl;
  std::string holder;
  for (int i=0; i < encrypted.size(); i++) {
    holder += encrypted[i]+",";
    //std::cout << encrypted[i] << std::endl; <-- if you want to output one at a time for some reason
  }
  holder.pop_back();
  std::cout << holder << std::endl;
  
  
  /*----------------DECRYPTION----------------------------------------------------
  If you have your own numbers to decrypt
  encrypted = {write your numbers in apostraphe's here with commas to seperate them}
  as an example I wrote one saying what my favorite RPG is
  
  encrypted = {"180918309867803811","142416121988924670","82781708593324780"};
  */
  std::cout << "Here is the decryption:" << std::endl;
  std::string eMessage;
  int flag = 0;
  for (int i=0; i < encrypted.size(); i++) {
    if (encrypted[i][0] == '0') {
      encrypted[i].erase(0, 1);
      flag += 1;
    }
    boost::multiprecision::cpp_int encryption = boost::lexical_cast < boost::multiprecision::cpp_int > (encrypted[i]);
    boost::multiprecision::cpp_int decipher = encryptDecrypt(encryption, d, n);
    if (flag == 1) {
      eMessage += "0" + boost::lexical_cast < std::string > (decipher);
      flag -= 1;
    } else {
      eMessage += boost::lexical_cast < std::string > (decipher);
    }
  }
  std::string final = convertToLetters(eMessage);
  std::cout << final << std::endl;
  return 0;
}

int main() {
  //Sample Usage
  RSA();
  return 0;
}

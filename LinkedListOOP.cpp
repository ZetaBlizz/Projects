#include<iostream>
#include<string>
#include<cmath>

using namespace std;


struct Node {
  int n; // data, an integer
  Node *next; //pointer to the next node
};

class LinkedList {
    private:
    Node *head;    //pointer to the first Node

   public:
    string original_string = "";
    LinkedList(){    //constructor
        head = NULL;  // set the head pointer to NULL value
    }
    LinkedList larger_number(LinkedList, LinkedList);

    LinkedList operator + (LinkedList B){
        LinkedList C;
        int num1 = stoi(original_string);
        int num2 = stoi(B.original_string);
        int total = num1+num2;
        C.generate(to_string(total));
        return C;
    }

        LinkedList operator * (LinkedList B){
        LinkedList C;
        int num1 = stoi(original_string);
        int num2 = stoi(B.original_string);
        int total = num1*num2;
        C.generate(to_string(total));
        return C;
    }

    void generate(string s) {
        original_string = s;
        string reversed = "";
        for(int i=s.length()-1; i>=0; --i){
            reversed += s[i];
        }


        int string_length = reversed.length();
        int counter = 0;
        while(counter != string_length) {
            int number = reversed[counter]-48;

            Node *tmp = new Node();
            tmp ->n = number;
            tmp ->next = head;
            head = tmp;
            counter +=1;
        }
    }

    int is_divisible_by(int x) {
        int i=0;
        int num = 0;
        int length = original_string.length()-1;
        while (i != original_string.length()){
            num += pow(4,length)*(original_string[i]-48);
            /*cout << "NUM: " << num << endl;
            cout << pow(4,length) << " <-EXPONENT, NUMBER -> " << original_string[i]-48 << endl;*/
            length -=1;
            i+=1;
        }
        if (num % x == 0)
            return 1;
        else
            return 0;
    }

     void digit_count() {
         Node *tmp = new Node();
         tmp = head;
         int zero = 0;
         int one = 0;
         int two = 0;
         int three = 0;

         while (tmp != NULL){
           int number = tmp->n;
           //cout << number << " in digit_count" << endl;
           switch(number) {
               case 0 :
                   //cout << number << " is a zero" << endl;
                   zero +=1;
                   break;
               case 1 :
                   //cout << number << " is a one" << endl;
                   one +=1;
                   break;
               case 2 :
                   //cout << number << " is a two" << endl;
                   two +=1;
                   break;
               case 3 :
                   //cout << number << " is a three" << endl;
                   three +=1;
                   break;
           }
           tmp = tmp->next;
         }
         cout << "0: " << zero << endl;
         cout << "1: " << one << endl;
         cout << "2: " << two << endl;
         cout << "3: " << three << endl;
    }

    int show_in_base_10(){
        int length = original_string.length()-1;
        int total = 0;
        Node *tmp = new Node();
        tmp = head;

        while (tmp != NULL){
        int number = tmp->n;
        total += pow(4, length)*number;
        //cout << "TOTAL: "<< pow(4,length) << " NUMBER: "<< number << endl;
        tmp = tmp->next;
        length -= 1;
        }
        return total;
    }

};

LinkedList larger_number(LinkedList B, LinkedList C){
        //cout << stoi(B.original_string) << " <-B C-> " << stoi(C.original_string) << endl;
        if (stoi(B.original_string) >  stoi(C.original_string))
            return B;
        else
            return C;
    }
    
int main {
	return 0;
}    
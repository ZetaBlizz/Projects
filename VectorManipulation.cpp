#include <iostream>
#include <string>
#include <cmath>

using namespace std;

struct Vector{
    double x;
    double y;
    double z;
};

Vector generate_vector(double a,double b,double c){
    Vector vectors;
    vectors.x = a;
    vectors.y = b;
    vectors.z = c;
    return vectors;
}

string show(Vector vectorDisplay){
    string s;
    s = "<"+to_string(vectorDisplay.x)+", "+to_string(vectorDisplay.y)+", "+to_string(vectorDisplay.z)+">";
    return s;
}

string normalize(Vector originalVector){
    Vector n;
    double length = sqrt(pow(originalVector.x,2)+pow(originalVector.y,2)+pow(originalVector.z,2));
    n.x = originalVector.x/length;
    n.y = originalVector.y/length;
    n.z = originalVector.z/length;
    return show(n);
}

double dot_product(Vector one, Vector two){
    return one.x*two.x + one.y*two.y + one.z*two.z;
}

string const_multiply(double a, Vector *originalVector){
    Vector m;
    m.x = a*originalVector->x;
    m.y = a*originalVector->y;
    m.z = a*originalVector->z;
    return show(m);
}

string cross_product(Vector *originalV1, Vector *originalV2){
    Vector o;
    o.x = originalV1->y*originalV2->z - originalV1->z*originalV2->y;
    o.y = originalV1->z*originalV2->x - originalV1->x*originalV2->z;
    o.z = originalV1->x*originalV2->y - originalV1->y*originalV2->x;
    return show(o);
}

string add(Vector *originalV1, Vector *originalV2){
    Vector p;
    p.x = originalV1->x + originalV2->x;
    p.y = originalV1->y + originalV2->y;
    p.z = originalV1->z + originalV2->z;
    return show(p);
}

int main() {
    Vector v1;
    Vector v2;
    /*this is how we generate Vectors */

    v1 = generate_vector(2,1,3);
    v2 = generate_vector(4,-5,8);
    /*output format of a Vector*/
    cout << show(v1) << endl; // prints to screen vector of the form <2.000000, 1.00000, 3.00000>
    cout << show(v2) << endl; // prints to screen vector of the form <4.000000, -5.00000, 8.00000>
    cout << normalize(v1) << endl; 
    cout << dot_product(v1, v2) << endl;
    cout << const_multiply(5, &v1) << endl;
    cout << cross_product(&v1, &v2) << endl
    cout << add(&v1, &v2) << endl;
    return 0;
}
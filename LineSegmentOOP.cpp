#include<iostream>
#include<vector>
#include<string>
#include<cmath>

using namespace std;

class Segment{
	private:
		vector<double> v1;
		vector<double> v2;
		friend string show(Segment);
		friend double getSegmentLength(Segment*);
	public:
		Segment(vector<double> a={0,0}, vector<double> b={0,0})
		{
		    v1= a;
            v2 = b;
		};
		Segment getLongerSegment(Segment, Segment);
		double getSlope();
		Segment operator + (Segment B){
            Segment C;
            C.v1[0] = v1[0]+B.v1[0];
            C.v1[1] = v1[1]+B.v1[1];
            C.v2[0] = v2[0]+B.v2[0];
            C.v2[1] = v2[1]+B.v2[1];
            return C;
		}
};

string show(Segment S) {
    return "Line segment between points ("+to_string(S.v1[0])+","+ to_string(S.v1[1])+") and (" +to_string(S.v2[0])+","+ to_string(S.v2[1])+").";;
}

double Segment::getSlope(){
    return (v2[1] - v1[1])/(v2[0] - v1[0]);
}

double getSegmentLength(Segment *A){
    return sqrt(pow(A->v2[0]-A->v1[0],2)+pow(A->v2[1]-A->v1[1],2));
}

Segment getLongerSegment(Segment A, Segment B){
    if (getSegmentLength(&A)>getSegmentLength(&B)){
        return A;
    } else {
        return B;
    }
}

int main{
	return 0
}
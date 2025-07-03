# include <iostream>
using namespace std;

class Arithmatic
{
    public:
        int no1, no2;

        Arithmatic(int A, int B)
        {
            this -> no1 = A;
            this -> no2 = B;
        }

        int Addition()
        {
            int Result = 0;
            Result = this->no1 + this-> no2;
            return Result;
        }

};

int main()
{
    Arithmatic obj(10, 11);
    
    int ret = 0;
    ret = obj.Addition();

    cout<< "Addition is : "<< ret<< endl;
    

    return 0;
}
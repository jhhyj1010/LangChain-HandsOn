#include <cstdlib>
#include <iostream>
#include <ostream>
#include <string>
#include <utility>
#include <vector>


using namespace std;
typedef std::vector<std::pair<std::string, int>> pairlist; // alias
typedef std::string text;
typedef int number_t;

using text_t = std::string; // better than typedef
using number_t = int;

namespace first {
    int x = 1;
}
namespace second {
    int x = 2;
}

int myNum = 0;

void bakePizza() {
    cout << "baking pizza" << endl;
}

void bakePizza(int a) {
    cout << "topping - " << a << endl;
}

void bakePizza(float a) {
    cout << "topping - " << a << endl;
}

void printNum() {
    int myNum = 2;
    cout << myNum <<endl;
}

template <typename T, typename U>
auto max(T x, U y) {
    cout << "Address of x is: " << &x << endl;
    return (x > y) ? x : y;
}

struct student {
    std::string name;
    double gpa;
    bool enrolled;
}Stu;

void swap(int &a, int &b) {
    cout << "In Swap, Address of a is: " << &a << " Address of b is: " << &b <<endl;
    int temp;
    temp = a;
    a = b;
    b = temp;
}

enum Day {
    Sun=0,
    Mon,
    Tue,
    Wed,
    Thu,
    Fri,
    Sat
};

class Employee {
    int a;
    text_t name;
    public:
        text_t get_name();
};

text_t Employee::get_name() {
    return this->name;
}

int main() {
    using std::string; //a secure way for avoiding any conflicts
    cout << "hello, jesson" << endl;
    cout << first::x << endl;
    cout << second::x << endl;

    string jesson = "hello";
    cout << jesson << endl;

    text wendy = "jieer";
    cout << wendy << endl;

    number_t age = 10;
    cout << age << endl;

    // string name;
    // cout << "please input a number:";
    // cin >> name;
    // cout << name <<endl;

    // int ch = round(3.1);
    // cout << ch <<endl;

    int grade = 80;
    grade >= 80 ? cout << "successful" <<endl : cout << "failed" <<endl;
    cout << (grade >= 80 ? "successful" : "failed") << endl;

    srand(time(NULL));
    int num = rand();
    cout << num % 6 << endl;

    int myNum = 1;
    cout << myNum << endl;

    printNum();
    cout << ::myNum << endl; // print the global myNum

    std:string name = "jesssdfsfsfssosfasfsafsafasfsafasn";
    string students[] = {"jesson", "wendy", "lucine"};
    cout << "size of int number is: " << sizeof(grade) << endl;
    cout << "size of string object is: " << sizeof(students) << endl;

    for (int i = 0; i < sizeof(students)/sizeof(string); i++) {
        cout << "student " << i << " is: " << students[i] << endl;
    }

    for (std::string student : students) { // foreach loop
        cout << student << endl;
    }

    string foods[100];
    cout << "starting index: " << foods << endl;
    fill(foods, foods+100, "pizza");
    // for (string item: foods) {
    //     cout << item << endl;
    // }

    int value = 100;
    int &rValue = value;
    cout << "value is " << value << " rValue is " << rValue << endl;
    rValue = grade;
    cout << "grade is " << rValue << endl;

    int *pInt = nullptr;

    cout << max(1.1, 3) << endl;

    Stu.name = "Lucine";
    Stu.enrolled = true;
    Stu.gpa = 4.5;

    int a=1, b=2;
    cout << "In the caller, address of a is: " << &a << " address of b is: " << &b << endl;
    swap(a, b);
    cout << "Numbers after swapping: a is: " << a << " b is: " << b <<endl;

    cout << "Sunday is " << Sat << endl;

    Employee emp1;
    cout << "name is: " << emp1.get_name() <<endl;
    // emp1.name = "jesson"; // illegal, the permission for class is Private by default

    return 0;
}
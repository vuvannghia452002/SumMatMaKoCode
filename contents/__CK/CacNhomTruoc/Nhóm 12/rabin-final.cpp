

#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int p = 331, q = 311; //private key pair(p,q) of the form 3 mod 4

int n = p * q;        //public key n

int encrypter(int m, int n)
{
    int c = (m * m) % n;    // c = (m^2) mod n
    return c;
}

//chinese remainder theorem implementation
int mod(int k, int b, int m)
{
    int i = 0;
    int a = 1;

    vector<int> t;
    while (k > 0) {
        t.push_back(k % 2);
        k = (k - t[i]) / 2;
        i++;
    }
    for (int j = 0; j < i; j++) {
        if (t[j] == 1) {
            a = (a * b) % m;
            b = (b * b) % m;
        }
        else {
            b = (b * b) % m;
        }
    }
    return a;
}

int modulo(int a, int b)
{
    return a >= 0 ? a % b : (b - abs(a % b)) % b;
}

//Extended Euclid
vector<int> Extended_Euclid(int a, int b)
{
    if (b > a) {
        int temp = a; a = b; b = temp;
    }
    int x = 0;
    int y = 1;
    int lastx = 1;
    int lasty = 0;
    while (b != 0) {
        int q = a / b;
        int temp1 = a % b;
        a = b;
        b = temp1;
        int temp2 = x;
        x = lastx - q * x;
        lastx = temp2;
        int temp3 = y;
        y = lasty - q * y;
        lasty = temp3;
    }
    vector<int>arr(3);
    arr[0] = lastx;
    arr[1] = lasty;
    arr[2] = 1;
    return arr;
}
// int
int decrypter(int c, int p, int q)
{
    int mp = mod((p + 1) / 4, c, p);
    int mq = mod((q + 1) / 4, c, q);

    vector<int> arr = Extended_Euclid(p, q);
    int rootp = arr[0] * p * mq;
    int rootq = arr[1] * q * mp;
    double r = modulo((rootp + rootq), n);
    if (r < 64)
        return r;
    int negative_r = n - r;
    if (negative_r < 64)
        return negative_r;
    int s = modulo((rootp - rootq), n);
    if (s > 64)
        return s;
    int negative_s = n - s;
    return negative_s;

}
//ascii
int decrypter_char(int c, int p, int q)
{
    int mp = mod((p + 1) / 4, c, p);
    int mq = mod((q + 1) / 4, c, q);

    vector<int> arr = Extended_Euclid(p, q);
    int rootp = arr[0] * p * mq;
    int rootq = arr[1] * q * mp;
    double r = modulo((rootp + rootq), n);
    if (r < 128)
        return r;
    int negative_r = n - r;
    if (negative_r < 128)
        return negative_r;
    int s = modulo((rootp - rootq), n);
    if (s < 128)
        return s;
    int negative_s = n - s;
    return negative_s;

}

int main()
{
    vector<int>e; //vector to store the encrypted message
    vector<int>d; //vector to store the decrypted message


    /*int message = 40569;
    cout << "Plain text: " << message << endl;

    cout << "Encrypted text: ";



        e.push_back(encrypter(message, n));
        cout << e[0];

    cout << endl;

        d.push_back(decrypter(encrypter(message, n ), p, q));

    cout << "Decrypted text: ";

        cout << int(d[0]);

    cout << endl;*/


    string message_char = "Nhom 12";
    cout << "Plain text: " << message_char << endl;
    int len = strlen(message_char.c_str());

    cout << "Encrypted text: ";

    for (int i = 0; i <= len; i++)
    {
        e.push_back(encrypter(message_char[i], n));
        cout << e[i];
    }

    cout << endl;

    for (int i = 0; i < len; i++)
    {
        d.push_back(decrypter_char(e[i], p, q));
    }
    cout << "Decrypted text: ";
    for (int i = 0; i < d.size(); i++)
        cout << char(d[i]);

    cout << endl;


    return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started:
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file

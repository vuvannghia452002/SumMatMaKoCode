using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CCA
{
    class Program
    {
        static void Main(string[] args)
        {           
            Console.WriteLine("Nhap khoa cong khai (n): ");           
            long  n = Convert.ToInt64(Console.ReadLine());     
            Console.WriteLine("---- y = x * x mod n----");
            Random rint = new Random();
            long x = (rint.Next(2, 1000));
            long y = (x * x) % n;
            Console.WriteLine("Thong tin: khoa cong khai n = {0}, ban ma: y = {1}", n, y);
            Console.WriteLine("1. Can bac 2 cua y: x = {0}", x);

            Console.WriteLine("Enter de tim khoa!");
            Console.ReadKey();

            Console.WriteLine("-----------Bat dau-----------");
            
            long q = gcd(Math.Abs(SqrtyModn(x, n, y) - x), n);
            long p = n / q;

            if (q == 0)
                Console.WriteLine("That bai!");
            else            
                Console.WriteLine("Khoa: p = {0}, q = {1}", p, q);
            
            Console.ReadKey();
        }
        static long SqrtyModn(long x, long n, long y)
        {
            long i;
            for(i = 1; i > 0; i++)
            {
                if ((i * i) % n == y % n && (x - i) % n != 0 && (x + i) % n != 0)
                    return i;
            }
            return 0;
        }

        static long gcd(long a, long b)
        {
            if (a == 0)
                return b;
            return gcd(b % a, a);
        }
    }
}

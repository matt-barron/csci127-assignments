#include <iostream>
#include <math.h>
int discriminant(int a, int b, int c)
{
  int d;
  int e;
  int f;
  d = 4 * a * c;
  e = b * b;
  f = e - d;
  return f;
}
int quadsolve(int a, int b, int c)
{
  int d;
  int j;
  int r;
  d = discriminant( a, b, c);
  j = sqrt(d);
  r = -1*b+j;
  if (d >= 0)
    {return r/2*a;}
  else
    {return 0;}
}
int main()
{
  int x = discriminant(2, 3, 4);
  int y = discriminant(-2, -3, -1);
  int z = discriminant( 1, 0, -5);
  int h = quadsolve( 2, 3, 4);
  int i = quadsolve( 1, 0, -5);
  std::cout<<"X = " <<x<<" Y =  "<< y<<" Z = "<< z<< "\n";
  std::cout<<"H = "<<h<< " I = "<<i<<"\n";
  return 0;

}

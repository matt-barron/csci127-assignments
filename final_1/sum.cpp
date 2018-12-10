#include <iostream>
int sumofsquares( int a, int b)
{
  int c;
  int  total;
  total = 0;
  for(c= a; c<=b; c++)
    {
      int g;
      g = c*c;
      total = total + g ;
    }
  return total;  
}
int main()
{
  int x = sumofsquares(5, 10);
  int y = sumofsquares(4,6);
  std::cout<<x<<" "<< y<<"\n";
  return 0;
}

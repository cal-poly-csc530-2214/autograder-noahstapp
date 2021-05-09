#include <cstdio>
#include <assert.h>
#include <iostream>
using namespace std;
#include "vops.h"
#include "translated.h"
namespace ANONYMOUS{

void main__Wrapper() {
  _main();
}
void main__WrapperNospec() {}
void _main() {
  int  n_s1=0;
  correction0(4, n_s1);
  int  m_s3=0;
  correction1(4, m_s3);
  assert ((((6 + m_s3) + n_s1)) == (23));;
}
void correction0(int n, int& _out) {
  _out = n + 1;
  return;
}
void correction1(int m, int& _out) {
  _out = 3 * m;
  return;
}

}

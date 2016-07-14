#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from challenge264easy import sort_code


def test_sort_code():
    input = """    sum = i + sum;
  {
  }
  int sum = 0;
  for (int i = 0; i <= 100; ++i)
  std::cout << sum;
  return 0;
{
}
#include <iostream>
int main()"""
    expected = """#include <iostream>
int main()
{
  int sum = 0;
  for (int i = 0; i <= 100; ++i)
  {
    sum = i + sum;
  }
  std::cout << sum;
  return 0;
}"""
    output = '\n'.join(sort_code(input))
    assert output == expected

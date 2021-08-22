"""
Example docstring using a ComplexNumber class

This module demonstrates the usage of docstrings within Python, following
Google's docstring Python Style Guide.

Todo:
    * Implement complex number multiplication, subtraction, and division
    * Implement complex number angle calculation
    * Write Sphinx documentation
"""

import math

class ComplexNumber:
    """
    This is a class for mathematical operations on complex numbers.

    This class is constant, always creating a new ComplexNumber object
    when doing operations. Ergo, safe for passing by reference.
      
    Attributes:
        real (int): The real part of complex number.
        imag (int): The imaginary part of complex number.
    """
  
    def __init__(self, real: float = 0.0, imag: float = 0.0):
        """
        The constructor for ComplexNumber class.
  
        Args:
           real (int): The real part of complex number (default 0.0).
           imag (int): The imaginary part of complex number (default 0.0).
        
        Raises:
            TypeError: if real or imag are not floats or ints
        """
        if type(real) not in [float, int]:
            raise TypeError("real part must be a float or int")

        if type(imag) not in [float, int]:
            raise TypeError("imag part must be a float or int")

        self._real = real
        self._imag = imag
    
    @property
    def real(self) -> float: return self._real

    @property
    def imag(self) -> float: return self._imag

    def add(self, num: ComplexNumber) -> ComplexNumber:
        """
        The function to add two Complex Numbers.
  
        Args:
            num (ComplexNumber): The complex number to be added.
          
        Returns:
            ComplexNumber: A complex number which contains the sum.
        
        Raises:
            TypeError: if num is not a ComplexNumber
        """
        if not isinstance(num, ComplexNumber):
            raise TypeError("num must be a ComplexNumber")
  
        real = self._real + num.real
        imag = self._imag + num.imag
  
        return ComplexNumber(real, imag)
    
    @property
    def magnitude(self):
        """Calculate the magnitude, or modulus, of the complex number."""
        return math.sqrt(self._real ** 2 + self._imag ** 2)
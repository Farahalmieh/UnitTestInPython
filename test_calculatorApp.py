import unittest
from unittest import mock
from unittest.mock import patch
from calculatorApp import *
import calculatorApp


class TestCalculate(unittest.TestCase):
    def setUp(self):
        print("Setup .. ")

    # Add
    def test_Add(self):
        self.assertEqual(add(6,4),10)

    def test_AddInvalid(self):
        self.assertNotEqual(add(5,4),10)

    # Subtract
    def test_Subtract(self):
        self.assertEqual(subtract(10,5), 5)

    def test_SubtractInvalid(self):
        self.assertNotEqual(subtract(5,3), 4)

    # Multiply
    def test_Multiply(self):
        self.assertEqual(multiply(10,5), 50)

    def test_MultiplyInvalid(self):
        self.assertNotEqual(multiply(9,3), 20)

    # Divide
    def test_Divide(self):
        self.assertEqual(divide(10,5), 2)
    
    def test_DivideByZero(self):
        self.assertRaises(ZeroDivisionError, divide, 1, 0)

    def test_DivideZeroByNum(self):
        self.assertEqual(divide(0,2),0)

    def test_DivideInvalid(self):
        self.assertNotEqual(divide(6,2),1)

    # Calculate
    def test_CalculateNull(self):
        self.assertRaises(ValueError, calculate, '2',None,None)
        self.assertRaises(ValueError, calculate, '2',None,2) 
        self.assertRaises(ValueError, calculate, '2',2,None)
        self.assertRaises(ValueError, calculate, '2',0,None)
        self.assertRaises(ValueError, calculate, '2',None,0)
        self.assertRaises(ValueError, calculate, '2',0,0)

    def test_CalculateInvalidInput(self):
        self.assertRaises(Exception, calculate, '7',6,5)
        self.assertRaises(Exception, calculate, 'x',6,5)
    
    def test_CalculateAdd(self):
        with mock.patch('calculatorApp.add', return_value = 5):
            result = calculate('1',4,1)
        self.assertEqual(result, 5)

    def test_CalculateSubtract(self):
        with mock.patch('calculatorApp.subtract', return_value = 10):
            result = calculate('2',20,10)
        self.assertEqual(result, 10)

    def test_CalculateMultiply(self):
        with mock.patch('calculatorApp.multiply', return_value = 200):
            result = calculate('3',20,10)
        self.assertEqual(result, (20, '*', 10, '=', 200))

    def test_CalculateDivide(self):
        with mock.patch('calculatorApp.divide', return_value = 2):
            result = calculate('4',20,10)
        self.assertEqual(result, (20, '/', 10, '=', 2))
    
    def test_CalculateDivideByZero(self):
        self.assertRaises(ZeroDivisionError, calculate, '4',20,'0') 
        self.assertRaises(ZeroDivisionError, calculate, '4',20,0) ## this will faild cause its invisable
        
    # isExit
    def test_isExitNo(self):
        self.assertTrue(isExit("no"))

    def test_isExitYes(self):
        self.assertFalse(isExit("yes"))

    def test_isExitInvalidInput(self):
        self.assertRaises(ValueError, isExit,'test_invalid')


    # Check User Input
    def test_CheckUserInputEmpty(self):
        self.assertRaises(ValueError, check_user_input,"")

    def test_CheckUserInputInt(self):
        self.assertEqual(check_user_input('50'), 50)

    def test_CheckUserInputFloat(self):
        self.assertEqual(check_user_input('55.55'), 55.55)

    def test_CheckUserInputInvalid(self):
        self.assertRaises(ValueError, check_user_input,"test_invalid")

    def tearDown(self):
        print("tearDown .. ")
        #self.patcher1.stop()#or add this and remove self.addCleanup(self.patcher1.stop) in startup but this is not recommened!

if __name__ == '__main__':
	unittest.main()

import pytest
from account import *

def test_init():
    testAcccount = Account('John')
    assert testAcccount.get_balance() == 0
    assert testAcccount.get_name() == 'John'
    testAcccount = Account('Noa')
    assert testAcccount.get_name() == 'Noa'

def test_deposit():
    testAccount = Account('John')
    assert testAccount.deposit(45) is True
    assert testAccount.deposit(0) is False
    assert testAccount.deposit(-1) is False
    #checking numerical values
    assert testAccount.get_balance() == 45
    testAccount.deposit(55)
    assert testAccount.get_balance() == 100
    testAccount.deposit(-1)
    assert testAccount.get_balance() == 100
    


import pytest
from account import *

def test_init():
    testAcccount = Account('John')
    assert testAcccount.get_balance() == 0
    assert testAcccount.get_name() == 'John'
    testAcccount = Account('Noa')
    assert testAcccount.get_name() == 'Noa'

def test_deposit():
    # checking boolean return - int
    testAccount = Account('John')
    assert testAccount.deposit(45) is True
    assert testAccount.deposit(0) is False
    assert testAccount.deposit(-1) is False
    # checking numerical values - int
    assert testAccount.get_balance() == 45
    testAccount.deposit(55)
    assert testAccount.get_balance() == 100
    testAccount.deposit(-1)
    assert testAccount.get_balance() == 100
    # checking boolean return - float
    assert testAccount.deposit(45.0) is True
    assert testAccount.deposit(0.0) is False
    assert testAccount.deposit(-1.0) is False
    # checking numerical values - float
    testAccount.deposit(1.1)
    assert testAccount.get_balance() == pytest.approx(146.1, abs=0.001)
    testAccount.deposit(5.5)
    assert testAccount.get_balance() == pytest.approx(151.6, abs=0.001)
    testAccount.deposit(-1.1)
    assert testAccount.get_balance() == pytest.approx(151.6, abs=0.001)
    # checking string values
    assert testAccount.deposit('Obama') is False
    testAccount.deposit('Obama')
    assert testAccount.get_balance() == pytest.approx(151.6, abs=0.001)

    

def test_withdraw():
    testAccount = Account('John')
    # checking boolean return - int
    assert testAccount.withdraw(0) is False
    testAccount.deposit(55)
    assert testAccount.withdraw(56) is False
    assert testAccount.withdraw(55) is True
    # checking numerical values - int
    testAccount.deposit(100)
    testAccount.withdraw(50)
    assert testAccount.get_balance() == 50
    testAccount.withdraw(50)
    assert testAccount.get_balance() == 0
    testAccount.withdraw(-1)
    assert testAccount.get_balance() == 0
    # checking boolean return - float
    testAccount.deposit(50.0)
    assert testAccount.withdraw(50.0) is True
    assert testAccount.withdraw(0.0) is False
    assert testAccount.withdraw(-1.1) is False
    

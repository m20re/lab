"""
 TODO: Finish documentation
"""

class Account:
    """
    A class representing a person's bank account
    """

    def __init__(self, name: str) -> None:
        """
        Constructor for initial state of account object
        :param name: A person's name.
        """
        self.__account_name = name
        self.__account_balance = float(0)
    
    def deposit(self, amount: float) -> bool:
        """
        Increments the __acount_balance by the given amt
        If the param <= 0, will return False
        :param amount: Increment amt
        :return: boolean value
        """
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True
    
    def withdraw(self, amount: float) -> bool: 
        """
        Decrements the __acount_balance by the given amt
        :param amount: Decrement amount
        :return: boolean value
        """
        if amount <= 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True
    
    def get_balance(self) -> float:
        """
        returns the balance as a float
        :return: the account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        returns the name as a string
        :return: the account name
        """
        return self.__account_name
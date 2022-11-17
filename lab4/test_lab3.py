import unittest

from index_lab3 import  CaloriesCalculator, CashCalculator, r1, r2, r3 ,r4 ,r5 ,r6, Calculator

class lab3Test(unittest.TestCase):
    
    def test_CaloriesCalculator(self):
        limit = 2500
        calories_calculator = CaloriesCalculator(limit)
        calories_calculator.add_record(r4)
        calories_calculator.add_record(r5)
        calories_calculator.add_record(r6)
        print(calories_calculator.get_calories_remained())#Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более 90 кКал
        return calories_calculator.get_calories_remained()
    
    def test_CaloriesValues(test_CaloriesCalculator):
        assert test_CaloriesCalculator, 'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более 90 кКал'

    def test_CashCalculator(self):
        cash_calculator = CashCalculator(1000)
        cash_calculator.add_record(r1)
        cash_calculator.add_record(r2)
        cash_calculator.add_record(r3)
        print(cash_calculator.get_today_cash_remained('rub'))#Денег нет, держись: твой долг -1259.0 руб
        return cash_calculator.get_today_cash_remained('rub')

    def test_CashValues(test_CashCalculator):
        assert test_CashCalculator, 'Денег нет, держись: твой долг -1259.0 руб'  

if __name__ == '__main__' :
    unittest.main()       
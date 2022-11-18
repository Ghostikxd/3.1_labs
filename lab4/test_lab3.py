import unittest

from index_lab3 import  CaloriesCalculator, CashCalculator, r1, r2, r3 ,r4 ,r5 ,r6, Calculator

class lab3Test(unittest.TestCase):
    
    def test_CaloriesCalculator(self):
        limit = 2500
        calories_calculator = CaloriesCalculator(limit)
        calories_calculator.add_record(r4)
        calories_calculator.add_record(r5)
        calories_calculator.add_record(r6)
        #Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более 1230 кКал
        self.assertEqual(calories_calculator.get_calories_remained(), 'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более 1230 кКал')
    
    def test_CashCalculator(self):
        cash_calculator = CashCalculator(1000)
        cash_calculator.add_record(r1)
        cash_calculator.add_record(r2)
        cash_calculator.add_record(r3)
        #Денег нет, держись: твой долг -568.0 руб
        self.assertEqual(cash_calculator.get_today_cash_remained('rub'), 'Денег нет, держись: твой долг -568.0 руб')

    def test_extra(self):
        calories_calculator=CaloriesCalculator(1000)
        calories_calculator.add_record(r4)
        self.assertEqual(calories_calculator.get_today_limit_balance(), -186)

    def test_currencies(self):
        cash_calculator = CashCalculator(3000)
        cash_calculator.add_record(r3)
        self.assertRaises(TypeError,cash_calculator.get_today_cash_remained('юань'))

if __name__ == '__main__' :
    unittest.main()       
class DatabaseHelper:
    database_conncetion = None
    data: str = ''

    def __new__(cls):
        if cls.database_conncetion is None:
            cls.database_conncetion: DatabaseHelper = object.__new__(cls)
            print('Подключение к БД')
        return cls.database_conncetion

    def select_data(self) -> str:
        return self.data

    def insert_data(self, new_data):
        self.data = new_data


if __name__ == '__main__':
    connection1 = DatabaseHelper()
    connection1.insert_data('123')
    connection2 = DatabaseHelper()
    print(connection2.select_data())
    connection3 = DatabaseHelper()
    connection3.insert_data('321')
    print(connection3.select_data())

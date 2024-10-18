def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
        return

    return


test_function()
inner_function()  # Ошибка - name 'inner_function' is not defined

class CustomError(Exception):
    def __init__(self, *args):
        super().__init__(*args)


def sum_valid_numbers(nums):
    count = 0
    for num in nums :
        if not isinstance(num, int):
            raise CustomError("adad na motabar yaft shod")
        count += num
    return count


my_num = [1, 2, 3, 5 ,'qasem', 6 ,8 ,9]


try:
    result = sum_valid_numbers(my_num)
    print(f"majmoe adad sahih{result}")
except CustomError as e:
    print(f"Error :{e}")
finally:
    print("payan amaliat jame")
    


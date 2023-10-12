from list import CustomList
import unittest

class TestList(unittest.TestCase):

    def setUp(self):
       pass

    def tearDown(self):
       pass

    def test_type_error_1(self):
        with self.assertRaises(TypeError):
            CustomList(1)

    def test_type_error_2(self):
        with self.assertRaises(TypeError):
            CustomList(1, {'key':3} , 6.78 , "str")

    def test_type_error_3(self):
        with self.assertRaises(TypeError):
            CustomList()

    def test_child_of_list(self):
        self.assertIn(list, CustomList.__mro__)

    def test_return_empty_list(self):
        cl = CustomList([])
        self.assertListEqual(cl,[])

    def test_return_list(self):
        cl = CustomList([1,2,3])
        self.assertListEqual(cl, [1,2,3])

    def test_return_empty_list(self):
        cl_1 = CustomList([])
        cl_2 = CustomList(cl_1)
        self.assertListEqual(cl_2, cl_1)
        self.assertListEqual(cl_2, [])

    def test_return_custom_list(self):
        cl_1 = CustomList([1,2,3])
        cl_2 = CustomList(cl_1)
        self.assertListEqual(cl_2, cl_1)
        self.assertListEqual(cl_2, [1,2,3])

    def test_assign_list(self):
        cl_1 = CustomList([1,2,3])
        cl_1 = [3,2,1]
        self.assertListEqual(cl_1, [3,2,1])

    def test_assign_custom_list(self):
        cl_1 = [1,2,3]
        cl_1 = CustomList([3,2,1])
        self.assertListEqual(cl_1, [3,2,1])

    def test_delete_empty_list(self):
        cl = CustomList([])
        del cl
        with self.assertRaises(UnboundLocalError):
            self.assertIsNone(cl, "")

    def test_delete_list(self):
        cl = CustomList([1,2,3])
        del cl
        with self.assertRaises(UnboundLocalError):
            self.assertIsNone(cl, "")







    #ТЕСТЫ НА ОШИБКИ ВВОДА ВХОДНЫХ ЗНАЧЕНИЙ

    def test_add_equal_lengths(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2  = CustomList([1,2,3,4,5])

        self.assertListEqual( cl_1.__add__(cl_2), [2,4,6,8,10])

    def test_add_non_equal_lengths(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2  = CustomList([1,2])

        self.assertListEqual(cl_1.__add__(cl_2), [2,4,3,4,5])

    def test_add_cl1_length_is_zero(self):
        cl_1 = CustomList([])
        cl_2  = CustomList([1,2])

        self.assertListEqual(cl_1.__add__(cl_2), [1,2])

    def test_add_cl2_length_is_zero(self):
        cl_1 = CustomList([1,2])
        cl_2  = CustomList([])

        self.assertListEqual(cl_1.__add__(cl_2), [1,2])

    def test_add_all_lengths_are_zero(self):
        cl_1 = CustomList([])
        cl_2  = CustomList([])

        self.assertListEqual(cl_1.__add__(cl_2), [])

    def test_add_new_list_is_the_new_obj(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl1_id = id(cl_1)
        cl_2  = CustomList([1,2,3])
        cl2_id = id(cl_2)

        res = cl_1.__add__(cl_2)

        self.assertNotEqual(id(res), cl1_id)
        self.assertNotEqual(id(res), cl2_id)

    def test_add_old_lists_are_the_old_obj(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl1_id = id(cl_1)
        cl_2  = CustomList([1,2,3])
        cl2_id = id(cl_2)

        cl_1.__add__(cl_2)

        self.assertEqual(cl1_id, id(cl_1))
        self.assertEqual(cl2_id, id(cl_2))


    # ТЕСТЫ НА НУЛИ В СПИСКАХ,ГДЕ МЕНЬШЕ ПЕРАМЕТРОВ
    # def test_add_cl1_less_length(self):
    #     cl_1 = CustomList([1,2])
    #     cl_2 = CustomList([1,2,3,4,5])

    #     cl_1.add(cl_2)

    def test(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2  = CustomList([1,2,3])
        print(cl_1+cl_2)




    



   
        






       



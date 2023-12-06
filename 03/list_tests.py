from list import CustomList
import unittest

class TestCustomList(unittest.TestCase):

    def setUp(self):
       pass

    def tearDown(self):
       pass

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

    def test_add_equal_lengths(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2  = CustomList([1,2,3,4,5])
        self.assertListEqual(cl_1+cl_2, [2,4,6,8,10])

    def test_add_non_equal_lengths(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2  = CustomList([1,2])

        self.assertListEqual(cl_1 + cl_2, [2,4,3,4,5])

    def test_add_cl1_length_is_zero(self):
        cl_1 = CustomList([])
        cl_2  = CustomList([1,2])
        self.assertListEqual(cl_1 + cl_2, [1,2])

    def test_add_cl2_length_is_zero(self):
        cl_1 = CustomList([1,2])
        cl_2  = CustomList([])

        self.assertListEqual(cl_1 + cl_2, [1,2])

    def test_add_all_lengths_are_zero(self):
        cl_1 = CustomList([])
        cl_2  = CustomList([])

        self.assertListEqual(cl_1 + cl_2, [])

    def test_add_new_list_is_the_new_obj(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl1 = cl_1
        cl_2  = CustomList([1,2,3])
        cl2 = cl_2

        res = cl_1 + cl_2

        self.assertNotEqual(id(res), id(cl1))
        self.assertNotEqual(res, cl1)
        self.assertNotEqual(id(res), id(cl2))
        self.assertNotEqual(res, cl2)

    def test_add_old_lists_are_the_old_obj(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl1 = cl_1
        cl_2  = CustomList([1,2,3])
        cl2 = cl_2

        cl_1.__add__(cl_2)

        self.assertEqual(id(cl1), id(cl_1))
        self.assertEqual(cl_1, cl1)
        self.assertEqual(id(cl2), id(cl_2))
        self.assertEqual(cl_2, cl2)

    def test_add_equal_lengths_cl2_is_list(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2  = [1,2,3,4,5]

        self.assertListEqual( cl_1 + cl_2, [2,4,6,8,10])

    def test_add_non_equal_lengths_cl2_is_list(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2  = [1,2]

        self.assertListEqual(cl_1+cl_2, [2,4,3,4,5])

    def test_add_cl1_length_is_zero_cl2_is_list(self):
        cl_1 = CustomList([])
        cl_2  = [1,2]

        self.assertListEqual(cl_1 + cl_2, [1,2])

    def test_add_cl2_length_is_zero_cl2_is_list(self):
        cl_1 = CustomList([1,2])
        cl_2  = []

        self.assertListEqual(cl_1 + cl_2, [1,2])

    def test_add_all_lengths_are_zero_cl2_is_list(self):
        cl_1 = CustomList([])
        cl_2  = []

        self.assertListEqual(cl_1 + cl_2, [])

    def test_add_new_list_is_the_new_obj_cl2_is_list(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl1_id = id(cl_1)
        cl_2  = [1,2,3]
        cl2_id = id(cl_2)

        res = cl_1 + cl_2

        self.assertNotEqual(id(res), cl1_id)
        self.assertNotEqual(id(res), cl2_id)

    def test_add_old_lists_are_the_old_obj_cl2_is_list(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl1_id = id(cl_1)
        cl_2  = [1,2,3]
        cl2_id = id(cl_2)

        cl_1.__add__(cl_2)

        self.assertEqual(cl1_id, id(cl_1))
        self.assertEqual(cl2_id, id(cl_2))


    def test_add_equal_lengths_cl1_is_list(self):
        cl_1 = [1,2,3,4,5]
        cl_2  = CustomList([1,2,3,4,5])

        self.assertListEqual( cl_1 + cl_2, [2,4,6,8,10])


    def test_add_non_equal_lengths_cl1_is_list(self):
        cl_1 = [1,2,3,4,5]
        cl_2  = CustomList([1,2])

        self.assertListEqual(cl_1 + cl_2, [2,4,3,4,5])

    def test_add_cl1_length_is_zero_cl1_is_list(self):
        cl_1 = []
        cl_2  = CustomList([1,2])

        self.assertListEqual(cl_1 + cl_2, [1,2])

    def test_add_cl2_length_is_zero_cl1_is_list(self):
        cl_1 = [1,2]
        cl_2  = CustomList([])

        self.assertListEqual(cl_1 + cl_2, [1,2])

    def test_add_all_lengths_are_zero_cl1_is_list(self):
        cl_1 = []
        cl_2  = CustomList([])

        self.assertListEqual(cl_1 + cl_2, [])

    def test_add_new_list_is_the_new_obj_cl1_is_list(self):
        cl_1 = [1,2,3,4,5]
        cl1_id = id(cl_1)
        cl_2  = CustomList([1,2,3])
        cl2_id = id(cl_2)

        res = cl_1 + cl_2

        self.assertNotEqual(id(res), cl1_id)
        self.assertNotEqual(id(res), cl2_id)

    def test_add_old_lists_are_the_old_obj_cl1_is_list(self):
        cl_1 = [1,2,3,4,5]
        cl1_id = id(cl_1)
        cl_2  = CustomList([1,2,3])
        cl2_id = id(cl_2)

        cl_1 + cl_2

        self.assertEqual(cl1_id, id(cl_1))
        self.assertEqual(cl2_id, id(cl_2))

    def test_add_equal_lengths_cl1_is_list(self):
        cl_1 = [1,2,3,4,5]
        cl_2  = CustomList([1,2,3,4,5])

        self.assertListEqual( cl_1 + cl_2, [2,4,6,8,10])


    def test_add_non_equal_lengths_cl1_is_list(self):
        cl_1 = [1,2,3,4,5]
        cl_2  = CustomList([1,2])

        self.assertListEqual(cl_1+cl_2, [2,4,3,4,5])

    def test_add_cl1_length_is_zero_cl1_is_list(self):
        cl_1 = []
        cl_2  = CustomList([1,2])

        self.assertListEqual(cl_1 + cl_2, [1,2])

    def test_add_cl2_length_is_zero_cl1_is_list(self):
        cl_1 = [1,2]
        cl_2  = CustomList([])

        self.assertListEqual(cl_1 + cl_2, [1,2])

    def test_add_all_lengths_are_zero_cl1_is_list(self):
        cl_1 = []
        cl_2  = CustomList([])

        self.assertListEqual(cl_1 + cl_2, [])

    def test_add_new_list_is_the_new_obj_cl1_is_list(self):
        cl_1 = [1,2,3,4,5]
        cl1_id = id(cl_1)
        cl_2  = CustomList([1,2,3])
        cl2_id = id(cl_2)

        res = cl_1 + cl_2

        self.assertNotEqual(id(res), cl1_id)
        self.assertNotEqual(id(res), cl2_id)

    def test_add_old_lists_are_the_old_obj_cl1_is_list(self):
        cl_1 = [1,2,3,4,5]
        cl1_id = id(cl_1)
        cl_2  = CustomList([1,2,3])
        cl2_id = id(cl_2)

        cl_1.__add__(cl_2)

        self.assertEqual(cl1_id, id(cl_1))
        self.assertEqual(cl2_id, id(cl_2))

    def test_sub_equal_lengths(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2  = CustomList([1,2,3,4,5])

        self.assertListEqual( cl_1 - cl_2, [0,0,0,0,0])

    def test_sub_non_equal_lengths(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2  = CustomList([1,2])

        self.assertListEqual(cl_1 - cl_2, [0,0,3,4,5])

    def test_sub_cl1_length_is_zero(self):
        cl_1 = CustomList([])
        cl_2  = CustomList([1,2])

        self.assertListEqual(cl_1 - cl_2, [-1,-2])

    def test_sub_cl2_length_is_zero(self):
        cl_1 = CustomList([1,2])
        cl_2  = CustomList([])

        self.assertListEqual(cl_1 - cl_2, [1,2])

    def test_sub_all_lengths_are_zero(self):
        cl_1 = CustomList([])
        cl_2  = CustomList([])

        self.assertListEqual(cl_1 - cl_2, [])

    def test_sub_new_list_is_the_new_obj(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl1 = cl_1
        cl_2  = CustomList([1,2,3])
        cl2 = cl_2

        res = cl_1 - cl_2

        self.assertNotEqual(id(res), id(cl1))
        self.assertNotEqual(res, cl1)
        self.assertNotEqual(id(res), id(cl2))
        self.assertNotEqual(res, cl2)

    def test_sub_old_lists_are_the_old_obj(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl1 = cl_1
        cl_2  = CustomList([1,2,3])
        cl2 = cl_2

        cl_1.__sub__(cl_2)

        self.assertEqual(id(cl1), id(cl_1))
        self.assertEqual(cl1, cl_1)
        self.assertEqual(id(cl2), id(cl_2))
        self.assertEqual(cl2, cl_2)


    def test_sub_equal_lengths_cl2_is_list(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2  = [1,2,3,4,5]

        self.assertListEqual( cl_1 - cl_2, [0,0,0,0,0])

    def test_sub_non_equal_lengths_cl2_is_list(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2  = [1,2]

        self.assertListEqual(cl_1 - cl_2, [0,0,3,4,5])

    def test_sub_cl1_length_is_zero_cl2_is_list(self):
        cl_1 = CustomList([])
        cl_2  = [1,2]

        self.assertListEqual(cl_1 - cl_2, [-1,-2])

    def test_sub_cl2_length_is_zero_cl2_is_list(self):
        cl_1 = CustomList([1,2])
        cl_2  = []

        self.assertListEqual(cl_1 - cl_2, [1,2])

    def test_sub_all_lengths_are_zero_cl2_is_list(self):
        cl_1 = CustomList([])
        cl_2  = []

        self.assertListEqual(cl_1 - cl_2, [])

    def test_sub_new_list_is_the_new_obj_cl2_is_list(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl1 = cl_1
        cl_2  = [1,2,3]
        cl2 = cl_2

        res = cl_1 - cl_2

        self.assertNotEqual(id(res), id(cl1))
        self.assertNotEqual(res, cl1)
        self.assertNotEqual(id(res), id(cl2))
        self.assertNotEqual(res, cl2)

    def test_sub_old_lists_are_the_old_obj_cl2_is_list(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl1 = cl_1
        cl_2  = [1,2,3]
        cl2 = cl_2

        cl_1.__sub__(cl_2)

        self.assertEqual(id(cl1), id(cl_1))
        self.assertEqual(cl1, cl_1)
        self.assertEqual(id(cl2), id(cl_2))
        self.assertEqual(cl2, cl_2)
    

    def test_sub_equal_lengths_cl1_is_list(self):
        cl_1 = [1,2,3,4,5]
        cl_2  = CustomList([1,2,3,4,5])

        self.assertListEqual( cl_1 - cl_2, [0,0,0,0,0])

    def test_sub_non_equal_lengths_cl1_is_list(self):
        cl_1 = [1,2,3,4,5]
        cl_2  = CustomList([1,2])

        self.assertListEqual(cl_1 - cl_2, [0,0,3,4,5])

    def test_sub_cl1_length_is_zero_cl1_is_list_cl1_is_list(self):
        cl_1 = []
        cl_2  = CustomList([1,2])

        self.assertListEqual(cl_1 - cl_2, [-1,-2])

    def test_sub_cl2_length_is_zero_cl1_is_list(self):
        cl_1 = [1,2]
        cl_2  = CustomList([])

        self.assertListEqual(cl_1 - cl_2, [1,2])

    def test_sub_all_lengths_are_zero_cl1_is_list(self):
        cl_1 = []
        cl_2  = CustomList([])

        self.assertListEqual(cl_1 - cl_2, [])

    def test_sub_new_list_is_the_new_obj_cl1_is_list(self):
        cl_1 = [1,2,3,4,5]
        cl1 = cl_1
        cl_2  = CustomList([1,2,3])
        cl2 = cl_2

        res = cl_1 - cl_2

        self.assertNotEqual(id(res), id(cl1))
        self.assertNotEqual(res, cl1)
        self.assertNotEqual(id(res), id(cl2))
        self.assertNotEqual(res, cl2)

    def test_str_empty_list(self):
        self.assertEqual(("[], 0"), str(CustomList([])))

    def test_str_not_empty_list(self):
        self.assertEqual(("[1, 2, 3, 4, 5], 15"), str(CustomList([1,2,3,4,5])))

    def test_str_one_elem_in_list(self):
        self.assertEqual(("[5], 5"), str(CustomList(CustomList([5]))))

    def test_eq_equal_lists(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2 = CustomList([3,5,7])
        self.assertEqual(True, cl_1==cl_2)
        self.assertEqual(True, cl_2==cl_1)

    def test_eq_not_equal_lists(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2 = CustomList([3,5,8])
        self.assertEqual(False, cl_1==cl_2)
        self.assertEqual(False, cl_2==cl_1)


    def test_ne_equal_lists(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2 = CustomList([3,5,7])
        self.assertEqual(False, cl_1!=cl_2)
        self.assertEqual(False, cl_2!=cl_1)


    def test_ne_not_equal_lists(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2 = CustomList([3,5,8])
        self.assertEqual(True, cl_1!=cl_2)
        self.assertEqual(True, cl_2!=cl_1)


    def test_gt_greater_list(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2 = CustomList([3,5,6])
        self.assertEqual(True, cl_1>cl_2)
        self.assertEqual(False, cl_2>cl_1)

    def test_gt_less_list(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2 = CustomList([3,5,8])
        self.assertEqual(False, cl_1>cl_2)
        self.assertEqual(True, cl_2>cl_1)



    def test_ge_equal_lists(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2 = CustomList([3,5,7])
        self.assertEqual(True, cl_1>=cl_2)
        self.assertEqual(True, cl_2>=cl_1)

    def test_ge_greater_list(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2 = CustomList([3,5,6])
        self.assertEqual(True, cl_1>=cl_2)
        self.assertEqual(False, cl_2>=cl_1)

    def test_ge_less_list(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2 = CustomList([3,5,8])
        self.assertEqual(False, cl_1>=cl_2)
        self.assertEqual(True, cl_2>=cl_1)



    def test_lt_greater_list(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2 = CustomList([3,5,6])
        self.assertEqual(False, cl_1<cl_2)
        self.assertEqual(True, cl_2<cl_1)

    def test_lt_less_list(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2 = CustomList([3,5,8])
        self.assertEqual(True, cl_1<cl_2)
        self.assertEqual(False, cl_2<cl_1)   


    def test_le_equal_lists(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2 = CustomList([3,5,7])
        self.assertEqual(True, cl_1<=cl_2)
        self.assertEqual(True, cl_2<=cl_1)

    def test_le_greater_list(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2 = CustomList([3,5,6])
        self.assertEqual(False, cl_1<=cl_2)
        self.assertEqual(True, cl_2<=cl_1)

    def test_le_less_list(self):
        cl_1 = CustomList([1,2,3,4,5])
        cl_2 = CustomList([3,5,8])
        self.assertEqual(True, cl_1<=cl_2)
        self.assertEqual(False, cl_2<=cl_1)

if __name__ == '__main__':
    unittest.main()
    


























    



   
        






       



class Solution:
    def calculate_expected_offspring(couples):
        exp = 0
        exp += 2 * (couples[0] + couples[1] + couples[2])
        exp += 1.5 * couples[3]
        exp += couples[4]
        print(exp)
    
    if "__main__" == __name__:
        calculate_expected_offspring(
            [
                17272, 18848, 17326, 16613, 16953, 16820
            ]
        )
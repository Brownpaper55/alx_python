def common_elements(set_1, set_2):
    c_sets = set_1 & set_2
    return c_sets

print(common_elements({ "Python", "C", "Javascript" },{ "Bash", "C", "Ruby", "Perl" }))
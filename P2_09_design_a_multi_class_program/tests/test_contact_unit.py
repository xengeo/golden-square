from lib.contact import Contact


"""
Given a name and number
name and number attributes return given values
"""
def test_name_and_number_returned_correctly():
    contact_1 = Contact('Name1', '076452347851')
    assert contact_1.name =='Name1'
    assert contact_1.number == '076452347851'


"""
Given a name and number
#format returns a user friendly string describing the contact
"""
def test_format_contact_name():
    contact_1 = Contact('Name1', '076452347851')
    assert contact_1.format() == "Name1: 076452347851"
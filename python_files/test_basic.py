#!/usr/bin/env python3

"""
Brian McDevitt
email: briandmcdevitt@gmail.com

Business Card Parser Unit Tests

This program parses the results of an optical character recognition (OCR) component 
in order to extract the name, phone number, and email address from the processed 
business card image.

RUN FORMAT:
$python test_basic.py

"""

import unittest
import main

class BasicTests(unittest.TestCase):

    """ Supplied Examples """

    def test_name_example1(self):
        contactInfo = main.parseFile("../examples/example1.txt")
        candidateName = contactInfo.getName()
        trueName = "John Doe"

        self.assertEqual(candidateName, trueName)


    def test_phone_example1(self):
        contactInfo = main.parseFile("../examples/example1.txt")
        candidatePhoneNumber = contactInfo.getPhoneNumber()
        truePhoneNumber = "4105551234"

        self.assertEqual(candidatePhoneNumber, truePhoneNumber)

    def test_email_example1(self):
        contactInfo = main.parseFile("../examples/example1.txt")
        candidateEmail = contactInfo.getEmailAddress()
        trueEmail = "john.doe@entegrasystems.com"

        self.assertEqual(candidateEmail, trueEmail)



    def test_name_example2(self):
        contactInfo = main.parseFile("../examples/example2.txt")
        candidateName = contactInfo.getName()
        trueName = "Jane Doe"

        self.assertEqual(candidateName, trueName)


    def test_phone_example2(self):
        contactInfo = main.parseFile("../examples/example2.txt")
        candidatePhoneNumber = contactInfo.getPhoneNumber()
        truePhoneNumber = "4105551234"

        self.assertEqual(candidatePhoneNumber, truePhoneNumber)

    def test_email_example2(self):
        contactInfo = main.parseFile("../examples/example2.txt")
        candidateEmail = contactInfo.getEmailAddress()
        trueEmail = "Jane.doe@acmetech.com"

        self.assertEqual(candidateEmail, trueEmail)



    def test_name_example3(self):
        contactInfo = main.parseFile("../examples/example3.txt")
        candidateName = contactInfo.getName()
        trueName = "Bob Smith"

        self.assertEqual(candidateName, trueName)


    def test_phone_example3(self):
        contactInfo = main.parseFile("../examples/example3.txt")
        candidatePhoneNumber = contactInfo.getPhoneNumber()
        truePhoneNumber = "17035551259"

        self.assertEqual(candidatePhoneNumber, truePhoneNumber)

    def test_email_example3(self):
        contactInfo = main.parseFile("../examples/example3.txt")
        candidateEmail = contactInfo.getEmailAddress()
        trueEmail = "bsmith@abctech.com"

        self.assertEqual(candidateEmail, trueEmail)


    """

    Another example with a less common name.

    """

    def test_name_example4(self):
        contactInfo = main.parseFile("../examples/example4.txt")
        candidateName = contactInfo.getName()
        trueName = "Meryl Streep"

        self.assertEqual(candidateName, trueName)


    def test_phone_example4(self):
        contactInfo = main.parseFile("../examples/example4.txt")
        candidatePhoneNumber = contactInfo.getPhoneNumber()
        truePhoneNumber = "8005554321"

        self.assertEqual(candidatePhoneNumber, truePhoneNumber)

    def test_email_example4(self):
        contactInfo = main.parseFile("../examples/example4.txt")
        candidateEmail = contactInfo.getEmailAddress()
        trueEmail = "meryl.streep@star.net"

        self.assertEqual(candidateEmail, trueEmail)

    """

    Example with unusual ordering of items.

    """


    def test_name_example5(self):
        contactInfo = main.parseFile("../examples/example5.txt")
        candidateName = contactInfo.getName()
        trueName = "Wallace Loh"

        self.assertEqual(candidateName, trueName)


    def test_phone_example5(self):
        contactInfo = main.parseFile("../examples/example5.txt")
        candidatePhoneNumber = contactInfo.getPhoneNumber()
        truePhoneNumber = "18005551234"

        self.assertEqual(candidatePhoneNumber, truePhoneNumber)

    def test_email_example5(self):
        contactInfo = main.parseFile("../examples/example5.txt")
        candidateEmail = contactInfo.getEmailAddress()
        trueEmail = "testudo.no1@umd.edu"

        self.assertEqual(candidateEmail, trueEmail)

    """

    Example with no phone number.

    """


    def test_name_example6(self):
        contactInfo = main.parseFile("../examples/example6.txt")
        candidateName = contactInfo.getName()
        trueName = "Jane Doe"

        self.assertEqual(candidateName, trueName)


    def test_phone_example6(self):
        contactInfo = main.parseFile("../examples/example6.txt")
        candidatePhoneNumber = contactInfo.getPhoneNumber()
        truePhoneNumber = "not found"

        self.assertEqual(candidatePhoneNumber, truePhoneNumber)

    def test_email_example6(self):
        contactInfo = main.parseFile("../examples/example6.txt")
        candidateEmail = contactInfo.getEmailAddress()
        trueEmail = "Jane.doe@acmetech.com"

        self.assertEqual(candidateEmail, trueEmail)


    """

    Example with no name or email adress.

    """


    def test_name_example7(self):
        contactInfo = main.parseFile("../examples/example7.txt")
        candidateName = contactInfo.getName()
        trueName = "not found"

        self.assertEqual(candidateName, trueName)


    def test_phone_example7(self):
        contactInfo = main.parseFile("../examples/example7.txt")
        candidatePhoneNumber = contactInfo.getPhoneNumber()
        truePhoneNumber = "4105551234"

        self.assertEqual(candidatePhoneNumber, truePhoneNumber)

    def test_email_example7(self):
        contactInfo = main.parseFile("../examples/example7.txt")
        candidateEmail = contactInfo.getEmailAddress()
        trueEmail = "not found"

        self.assertEqual(candidateEmail, trueEmail)


if __name__ == "__main__":
    unittest.main()
